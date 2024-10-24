# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import random
import yamale
from .yaml_validator.custom_validator import validators
import yaml
from jinja2 import Environment, FileSystemLoader
import autopep8
from .utils import (
    file_exists,
    create_directory,
    directory_exists,
    is_directory,
    read_yaml_to_dict,
    calculate_cron_schedule,
    load_source
)
from .rules import (
    Rule
)


class Engine():
    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
        dag_divider="PARENT_FOLDER",
    ):
        self.DAGs = []
        self.baseline_imports = []
        self.templates = {}
        self.templates_count = 0
        self.templates_path = templates_path
        self.config = {}
        self.config_file = config_file
        self.source_path = source_path
        source_xml_name = self.source_path.split("/")[-1].split(".")[0]
        self.output_path = f"{output_path}/{source_xml_name}"
        self.dag_divider = dag_divider
        self.schema = "./dagify/converter/yaml_validator/schema.yaml"
        self.uf = load_source(self.source_path)

        # Run the Proccess
        self.set_baseline_imports()
        self.load_config()
        self.load_templates()
        self.validate()
        self.convert()
        self.cal_dag_dividers()
        self.calc_dag_dependencies()
        self.generate_airflow_dags()

    def load_config(self):
        # Validate Template Path Provided
        if self.config_file is None:
            raise ValueError("dagify: config file not provided")
        if file_exists(self.config_file) is False:
            raise FileNotFoundError("dagify: config file does not exist")

        with open(self.config_file) as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc

        if self.config is None:
            raise ValueError("dagify: No configuration has been loaded")

        if self.config["config"]["mappings"] is None:
            raise ValueError(
                "dagify: Configuration loaded with error, no Operator/JobType Mappings loaded")

        # Modify Configration for Standardization:
        templatesToValidate = []
        for idx, config in enumerate(self.config["config"]["mappings"]):
            # Set Command Uppercase
            self.config["config"]["mappings"][idx]["job_type"] = \
                self.config["config"]["mappings"][idx]["job_type"].upper()
            templatesToValidate.append(self.config["config"]["mappings"][idx]["template_name"])

        for root, dirs, files in os.walk(self.templates_path):
            for file in files:
                if file.endswith(".yaml"):
                    template_name = file.split(".")[0]
                    if template_name in templatesToValidate:
                        print(f"{template_name} ready for validation")
                    # Loads a Single Template into a Dictionary from .yaml file

                        file_path = os.path.join(root, file)
                        template = yamale.make_data(file_path)
                        schema = yamale.make_schema(self.schema, validators=validators)

                        if template is not None:

                            try:

                                yamale.validate(schema, template)
                                print(f"Validation succeeded for {file}!")

                            except yamale.YamaleError as e:
                                print(f"Validation failed for {file}!\n")
                                for result in e.results:
                                    for error in result.errors:
                                        print(error)
                                raise ValueError(f"Template {file_path} incompatible")

        return

    def validate(self):
        # TODO
        # Check that every Job in the Source has a Configured Mapping in Config
        # Check that every JobType in Config has a Template Name and that that
        # Template Name is in Templates;

        if self.output_path is None:
            raise ValueError("dagify: No output path provided")
        if directory_exists(self.output_path) is False:
            create_directory(self.output_path)

        return

    def load_templates(self):
        # This will load all templates from the provide path into a universal
        # HashMap for Direct Referencing

        # Validate Template Path Provided
        if self.templates_path is None:
            raise ValueError("dagify: Templates path not provided")
        if is_directory(self.templates_path) is False:
            raise NotADirectoryError(
                "dagify: Templates path is not a directory")

        # Load Templates
        for root, dirs, files in os.walk(self.templates_path):
            for file in files:
                if file.endswith(".yaml"):
                    # Loads a Single Template into a Dictionary from .yaml file
                    template = read_yaml_to_dict(os.path.join(root, file))
                    if template is not None:
                        # if the dict it not empty
                        self.templates_count += 1
                        self.templates[template["metadata"]["name"]] = template
        return

    def get_template_count(self):
        return self.templates_count

    def calc_dag_dependencies(self):
        self.uf.calculate_dag_dependencies()
        return

    def generate_dag_dependency_statements(self):
        self.uf.generate_dag_dependency_statements(self.dag_divider)
        return

    def generate_ext_task_marker_statement(self, task, ext_dag_id, ext_task_id):
        pass

    def cal_dag_dividers(self):
        dag_dividers = []
        for tIdx, task in enumerate(self.uf.get_tasks()):
            td = task.get_attribute(self.dag_divider)
            if td is not None and td not in dag_dividers:
                dag_dividers.append(td)
            task.set_dag_name(td)
        self.dag_dividers = dag_dividers

        return

    def get_dag_dividers(self):
        return self.dag_dividers

    def convert(self):
        if self.uf is None:
            raise ValueError(
                "dagify: no data in universal format. nothing to convert!")

        # process the conversion of all universal format items
        for tIdx, task in enumerate(self.uf.get_tasks()):
            # process a single task
            task_type = task.get_attribute("TASKTYPE")
            task_name = task.get_attribute("JOBNAME")
            if task_type is None:
                raise ValueError(
                    f"dagify: no task/job_type in source for task {task_name}")
            template_name = self.get_template_name(task_type)
            # get the template from the template name
            # [0][0] as the template dictionary is the first element of a tuple, in turn first element of a list
            template = self.get_template(template_name)
            if template is None:
                raise ValueError(
                    f"dagify: no template name provided that matches job type {task_type}")

            src_platform_name = template["source"]["platform"].get(
                "name", "UNKNOWN_SOURCE_PLATFORM")
            src_operator_name = template["source"]["operator"].get(
                "id", "UNKNOWN_SOURCE_PLATFORM")
            tgt_platform_name = template["target"]["platform"].get(
                "name", "UNKNOWN_TARGET_PLATFORM")
            tgt_operator_name = template["target"]["operator"].get(
                "name", "UNKNOWN_TARGET_PLATFORM")
            print(
                f" --> Converting Job number {str(tIdx)}: {task_name}, \n \
\t from Source Platform {src_platform_name} to Target Platform: {tgt_platform_name}\n \
\t from Source Operator {src_operator_name} to Target Operator: {tgt_operator_name}\n \
\t with template: {template_name}\n")

            output = airflow_task_build(task, template)
            task.set_airflow_task_output(output)

            python_imports = airflow_task_python_imports_build(task, template)
            task.set_airflow_task_python_imports(python_imports)

    def get_template(self, template_name):
        # Validate template_name is Provided
        if template_name is None:
            # raise ValueError("dagify: template name must be provided")
            template = self.templates.get("control-m-dummy-to-airflow-dummy", None)
        else:
            template = self.templates.get(template_name, None)
        if template is None:
            raise ValueError(
                f"dagify: no template with name: '{template_name}' was not found among loaded templates.")
        return template

    # TODO Add Filter Support (Multiple Templates by Filters)

    def get_template_name(self, job_type):
        for mapping in self.config["config"]["mappings"]:
            if mapping["job_type"] == job_type.upper():
                return mapping["template_name"]
        # no match found
        return None

    def generate_airflow_dags(self):

        if self.uf is None:
            raise ValueError("dagify: no data in universal format. nothing to convert!")

        for tIdx, dag_divider_value in enumerate(self.get_dag_dividers()):
            airflow_task_outputs = []
            tasks = []
            schedule_interval = None
            for tIdx, task in enumerate(self.uf.get_tasks()):
                # Capture the airflow tasks for each dag divider
                if task.get_attribute(self.dag_divider) == dag_divider_value:
                    tasks.append(task.get_attribute("JOBNAME_ORIGINAL"))
                    airflow_task_outputs.append(task.get_airflow_task_output())
                    if not schedule_interval:
                        schedule_interval = calculate_cron_schedule(task)

            # Calculate DAG Specific Python Imports
            dag_python_imports = self.uf.calculate_dag_python_imports(
                dag_divider_key=self.dag_divider,
                dag_divider_value=dag_divider_value
            )

            # Calculate all internal and external task dependencies
            dependencies = self.uf.generate_dag_dependencies_by_divider(self.dag_divider)
            dependencies_in_dag_internal = []
            dependencies_in_dag_external = []
            for task in tasks:
                if len(dependencies[dag_divider_value][task]['internal']) > 0:
                    dependencies_in_dag_internal.append(self.uf.generate_dag_dependency_statement(task, dependencies[dag_divider_value][task]['internal']))

                for dep in dependencies[dag_divider_value][task]['external']:
                    ext_task_uf = self.uf.get_task_by_attr("JOBNAME_ORIGINAL", dep)
                    dependencies_in_dag_external.append({
                        'task_name': task,
                        'ext_dag': ext_task_uf.get_attribute(self.dag_divider),
                        'ext_dep_task': dep,
                        "marker_name": dep + "_marker_" + ''.join(random.choices('0123456789abcdef', k=4))
                    })

            # Calculate external upstream dependencies where a task in the current dag depends on another dag's task
            # Such a dependency will require a DAG Sensor
            # The approach that is implemented is to iterate over all external dependencies in the dependencies dictionary and identify the tasks that
            # are also in the current dag.
            upstream_dependencies = []

            for _, divider_tasks in dependencies.items():
                for task, int_ext_deps in divider_tasks.items():
                    ext_deps = int_ext_deps["external"]
                    for ext_dep in ext_deps:
                        if ext_dep in tasks:
                            ext_task_uf = self.uf.get_task_by_attr("JOBNAME_ORIGINAL", task)
                            upstream_dag_name = ext_task_uf.get_attribute(self.dag_divider)

                            upstream_dependencies.append({
                                "task_name": ext_dep,
                                "task_in_upstream_dag": task,
                                "upstream_dag_name": upstream_dag_name,
                                "sensor_name": ext_dep + "_sensor_" + ''.join(random.choices('0123456789abcdef', k=4))
                            })

            # Get DAG Template
            environment = Environment(
                loader=FileSystemLoader("./dagify/converter/templates/"))
            template = environment.get_template("dag.tmpl")

            if directory_exists(self.output_path) is False:
                create_directory(self.output_path)

            # Create DAG File by Folder
            filename = f"{self.output_path}/{dag_divider_value}.py"

            content = template.render(
                baseline_imports=self.get_baseline_imports(),
                custom_imports=dag_python_imports,
                dag_id=dag_divider_value,
                schedule_interval=schedule_interval,
                tasks=airflow_task_outputs,
                dependencies_int=dependencies_in_dag_internal,
                dependencies_ext=dependencies_in_dag_external,
                upstream_dependencies=upstream_dependencies
            )
            with open(filename, mode="w", encoding="utf-8") as dag_file:
                content_linted = autopep8.fix_code(content)
                dag_file.write(content_linted)

        return

    def set_baseline_imports(self):
        self.baseline_imports = [
            "from airflow import DAG",
            "from airflow.decorators import task",
            "from airflow.sensors.external_task import ExternalTaskMarker",
            "from airflow.sensors.external_task import ExternalTaskSensor",
            "import datetime"
        ]
        return

    def get_baseline_imports(self):
        return self.baseline_imports


def airflow_task_build(task, template):
    # Load the Template Output Structure
    if template["structure"] is None:
        raise ValueError(
            f"dagify: no output structure in template: {template['metadata']['name']}, conversion will perform no action")

    if template["mappings"] is None:
        raise ValueError(
            f"dagify: no mappings in template: {template['metadata']['name']}, conversion will perform no action")

    # Declare Output Values Dictionary
    values = {}

    # Process each Mapping
    for mapping in template["mappings"]:
        # Lookup Mapping Target Key
        targetKey = mapping.get('target', None)
        if targetKey is None:
            # If Key is None, Skip
            continue

        # Load Target Value or Default Value for TargetKey from task source
        # field
        targetValue = task.get_attribute(mapping.get("source", ""))

        # Apply Rules
        # TODO: Handle Rules through additional function
        rules = mapping.get("rules", [])
        if rules is None:
            rules = []

        if len(rules) == 0:
            print("No Rules applied to source during mapping")

        for rule in rules:
            print(f"Apply Rule {rule.get('rule')}")
            r = Rule()
            args = [rule.get("rule"), targetValue]
            for arg in rule.get("args", []):
                args.append(arg)
            targetValue = r.run(args)

            # Update the Current Object Value
            task.set_attribute(mapping.get("source", ""), targetValue)

        if targetValue is None:
            # TODO - Log That we are going to use the defaults
            targetValue = mapping.get("default", None)
        if targetValue is None:
            # TODO - Log No Default Found, Handle with !UNKNOWN!!
            targetValue = "!!UNKNOWN!!"
        # Construct Values for Output!
        values[targetKey] = targetValue

    # Explicit Trigger Rule Handling
    # By default, the trigger rule will be all_success unless there is an in-condition with "OR" relationship
    trigger_rule = "all_success"
    for in_condition in task.get_in_conditions():
        if in_condition.get_attribute("AND_OR") == 'O':
            trigger_rule = 'one_success'
    values["trigger_rule"] = trigger_rule

    # Construct Output Python Object Text
    output = template["structure"].format(**values)
    return output


def airflow_task_python_imports_build(task, template):
    # Load the Template Output Structure
    if template["target"] is None:
        raise ValueError(
            f"dagify: no target data in template: {template['metadata']['name']}, python imports can not be calculated")
    if template["target"]['operator'] is None:
        raise ValueError(
            f"dagify: no target operator data in template: {template['metadata']['name']}, python imports can not be calculated")
    if template["target"]['operator']['imports'] is None:
        raise ValueError(
            f"dagify: no target operator import data in template: {template['metadata']['name']}, python imports can not be calculated")

    python_imports = []
    for imp in template["target"]['operator']['imports']:
        if imp['package'] is None:
            continue
        if imp['imports'] is None:
            continue
        if len(imp['imports']) is None:
            continue
        python_imports.append(imp)
    return python_imports
