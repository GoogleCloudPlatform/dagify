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
import yaml
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
from .utils import (
    file_exists,
    create_directory,
    directory_extist,
    is_directory,
    read_yaml_to_dict,
)
from .uf import (
    UF,
    UFFolder,
    UFTask,
    UFTaskVariable,
    UFTaskInCondition,
    UFTaskOutCondition,
    UFTaskShout,
)

class Engine():
    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
    ):
        self.DAGs = []
        self.baseline_imports = []
        self.templates = {}
        self.templates_count = 0
        self.templates_path = templates_path
        self.config = {}
        self.config_file = config_file
        self.source_path = source_path
        self.output_path = output_path

        # Run the Proccess
        self.set_baseline_imports()
        self.load_config()
        self.load_templates()
        self.load_source()
        self.validate()
        self.convert()
        self.calc_dependencies()
        self.generate_airflow_dags()

    def load_config(self):
        # Validate Template Path Provided
        if self.config_file is None:
            raise ValueError("AirShip: config file not provided")
        if file_exists(self.config_file) is False:
            raise FileNotFoundError("AirShip: config file does not exist")

        with open(self.config_file) as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc

        if self.config is None:
            raise ValueError("AirShip: No configuration has been loaded")

        if self.config["config"]["mappings"] is None:
            raise ValueError(
                "AirShip: Configuration loaded with error, no Operator/JobType Mappings loaded")

        # Modify Configration for Standardization:
        for idx, config in enumerate(self.config["config"]["mappings"]):
            # Set Command Uppercase
            self.config["config"]["mappings"][idx]["job_type"] = \
                self.config["config"]["mappings"][idx]["job_type"].upper()
        return

    def validate(self):
        # TODO
        # Check that every Job in the Source has a Configured Mapping in Config
        # Check that every JobType in Config has a Template Name and that that
        # Template Name is in Templates;

        if self.output_path is None:
            raise ValueError("AirShip: No output path provided")
        if directory_extist(self.output_path) is False:
            create_directory(self.output_path)
        return

    def load_templates(self):
        # This will load all templates from the provide path into a universal
        # HashMap for Direct Referencing

        # Validate Template Path Provided
        if self.templates_path is None:
            raise ValueError("AirShip: Templates path not provided")
        if is_directory(self.templates_path) is False:
            raise NotADirectoryError(
                "AirShip: Templates path is not a directory")

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

    def load_source(self):
        # Read the Source File
        # Parse into AirShip Universial Format
        # Output the AirShip Universial Format Back to the Class
        self.universal_format = None
        if self.source_path is None:
            raise ValueError("AirShip: source file cannot be None or Empty")
        if file_exists(self.source_path) is False:
            raise FileNotFoundError(
                "AirShip: source file not found at {}".format(
                    self.source_path))

        root = ET.parse(self.source_path).getroot()
        self.uf = self.parse_universal_format(root)
        return

    def parse_universal_format(self, source):
        uf = UF()
        uf = self.parse_controlm_tree(source, uf)
        return uf

    def parse_controlm_tree(self, root_node, parent):
        for node in root_node:
            match node.tag:
                case "FOLDER" | "SMART_FOLDER":
                    ufFolder = UFFolder()
                    ufFolder.from_controlm_xml(node)
                    parent.add_folder(ufFolder)
                    self.parse_controlm_tree(node, ufFolder)
                case "JOB":
                    ufTask = UFTask()
                    ufTask.from_controlm_xml(node)
                    parent.add_task(ufTask)
                    self.parse_controlm_tree(node, ufTask)
                case "VARIABLE":
                    ufTaskVariable = UFTaskVariable()
                    ufTaskVariable.from_controlm_xml(node)
                    parent.add_variable(ufTaskVariable)
                    self.parse_controlm_tree(node, ufTaskVariable)
                case "INCOND":
                    ufTaskInCondition = UFTaskInCondition()
                    ufTaskInCondition.from_controlm_xml(node)
                    parent.add_in_condition(ufTaskInCondition)
                    self.parse_controlm_tree(node, ufTaskInCondition)
                case "OUTCOND":
                    ufTaskOutCondition = UFTaskOutCondition()
                    ufTaskOutCondition.from_controlm_xml(node)
                    parent.add_out_condition(ufTaskOutCondition)
                    self.parse_controlm_tree(node, ufTaskOutCondition)
                case "SHOUT":
                    ufTaskShout = UFTaskShout()
                    ufTaskShout.from_controlm_xml(node)
                    parent.add_shout(ufTaskShout)
                    self.parse_controlm_tree(node, ufTaskShout)
                case _:
                    print("Node: " + node.tag + " is not currently supported.")

        return parent

    def parse_universal_format(self, source):
        uf = UF()
        uf = self.parse_controlm_tree(source, uf)
        return uf

    def parse_controlm_tree(self, root_node, parent):
        for node in root_node:
            match node.tag:
                case "FOLDER" | "SMART_FOLDER":
                    ufFolder = UFFolder()
                    ufFolder.from_controlm_xml(node)
                    parent.add_folder(ufFolder)
                    self.parse_controlm_tree(node, ufFolder)
                case "JOB":
                    ufTask = UFTask()
                    ufTask.from_controlm_xml(node)
                    parent.add_task(ufTask)
                    self.parse_controlm_tree(node, ufTask)
                case "VARIABLE":
                    ufTaskVariable = UFTaskVariable()
                    ufTaskVariable.from_controlm_xml(node)
                    parent.add_variable(ufTaskVariable)
                    self.parse_controlm_tree(node, ufTaskVariable)
                case "INCOND":
                    ufTaskInCondition = UFTaskInCondition()
                    ufTaskInCondition.from_controlm_xml(node)
                    parent.add_in_condition(ufTaskInCondition)
                    self.parse_controlm_tree(node, ufTaskInCondition)
                case "OUTCOND":
                    ufTaskOutCondition = UFTaskOutCondition()
                    ufTaskOutCondition.from_controlm_xml(node)
                    parent.add_out_condition(ufTaskOutCondition)
                    self.parse_controlm_tree(node, ufTaskOutCondition)
                case "SHOUT":
                    ufTaskShout = UFTaskShout()
                    ufTaskShout.from_controlm_xml(node)
                    parent.add_shout(ufTaskShout)
                    self.parse_controlm_tree(node, ufTaskShout)
                case _:
                    print("Node: " + node.tag + " is not currently supported.")

        return parent

    def calc_dependencies(self):

        for fIdx, folder in enumerate(self.uf.get_folders()):
            folder.calculate_dag_dependencies()
        return

    def convert(self):
        if self.uf is None:
            raise ValueError(
                "AirShip: no data in universal format. nothing to convert!")

        # process the conversion of all universal format items
        for fIdx, folder in enumerate(self.uf.get_folders()):
            # process a single folder
            for tIdx, task in enumerate(folder.get_tasks()):
                # process a single task
                task_type = task.get_attribute("TASKTYPE")
                task_name = task.get_attribute("JOBNAME")
                if task_type is None:
                    raise ValueError(
                        f"AirShip: no task/job_type in source for task {task_name}")
                template_name = self.get_template_name(task_type)
                # get the template from the template name
                template = self.get_template(template_name)
                if template is None:
                    raise ValueError(
                        f"AirShip: no template name provided that matches job type {task_type}")

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
                # imports = airflow_imports_build(task, template)
                task.set_output_airflow_task(output)


    def convert(self):
        if self.uf is None:
            raise ValueError(
                "AirShip: no data in universal format. nothing to convert!")

        # process the conversion of all universal format items
        for fIdx, folder in enumerate(self.uf.get_folders()):
            # process a single folder
            for tIdx, task in enumerate(folder.get_tasks()):
                # process a single task
                task_type = task.get_attribute("TASKTYPE")
                task_name = task.get_attribute("JOBNAME")
                if task_type is None:
                    raise ValueError(
                        f"AirShip: no task/job_type in source for task {task_name}")
                template_name = self.get_template_name(task_type)
                # get the template from the template name
                template = self.get_template(template_name)
                if template is None:
                    raise ValueError(
                        f"AirShip: no template name provided that matches job type {task_type}")

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
            raise ValueError("AirShip: template name must be provided")
        template = self.templates.get(template_name, None)
        if template is None:
            raise ValueError(
                f"AirShip: no template with name: '{template_name}' was not found among loaded templates.")
        return template

    # TODO Add Filter Support (Multiple Templates by Filters)

    def get_template_name(self, job_type):
        for mapping in self.config["config"]["mappings"]:
            if mapping["job_type"] == job_type.upper():
                return mapping["template_name"]
        # no match found
        return None

    def get_distinct_job_types(self):
        job_types = []
        # iterate all folders
        for folder in self.universal_format:
            # iterate all jobs within a folder
            for job in self.universal_format[folder]["jobs"]:
                # capture the job task type
                job_types.append(
                    self.universal_format[folder]["jobs"][job]["task_type"].upper())

        # return distinct set of job types
        return list(set(job_types))

    def generate_airflow_dags(self):

        if self.uf is None:
            raise ValueError("AirShip: no data in universal format. nothing to convert!")

        # imports = []
        # dag_id = ""
        tasks = []
        # dependencies = []

        # process the conversion of all universal format items
        for fIdx, folder in enumerate(self.uf.get_folders()):
            # process a single folder
            for tIdx, task in enumerate(folder.get_tasks()):
                # Capture the airflow tasks
                tasks.append(task.get_output_airflow_task())
                # Capture the airflow task imports
                # tasks.append(task.get_output_airflow_task())

                # Get DAG Template
                environment = Environment(
                    loader=FileSystemLoader("./AirShip/converter/templates/"))
                template = environment.get_template("dag.tmpl")

                if directory_extist(self.output_path) is False:
                    create_directory(self.output_path)

            # Create DAG File by Folder
            filename = f"output/{folder.get_attribute('FOLDER_NAME')}.py"
            content = template.render(
                # imports=folder.calculate_imports(),
                dag_id=folder.get_attribute("FOLDER_NAME"),
                tasks=tasks,
                # dependencies=folder.calculate_job_dependencies()
            )
            with open(filename, mode="w", encoding="utf-8") as dag_file:
                dag_file.write(content)

        return

    def generate_airflow_dags(self):

        if self.uf is None:
            raise ValueError("AirShip: no data in universal format. nothing to convert!")

        # imports = []
        # dag_id = ""
        tasks = []
        # dependencies = []

        # process the conversion of all universal format items
        for fIdx, folder in enumerate(self.uf.get_folders()):
            folder.calculate_dag_dependencies()
            folder.calculate_dag_python_imports()
            # process a single folder
            for tIdx, task in enumerate(folder.get_tasks()):
                # Capture the airflow tasks
                tasks.append(task.get_airflow_task_output())
                # Capture the airflow task imports
                # tasks.append(task.get_airflow_task_output())

            # Get DAG Template
            environment = Environment(
                loader=FileSystemLoader("./AirShip/converter/templates/"))
            template = environment.get_template("dag.tmpl")

            if directory_extist(self.output_path) is False:
                create_directory(self.output_path)
                    
                

            # Create DAG File by Folder
            filename = f"output/{folder.get_attribute('FOLDER_NAME')}.py"
            content = template.render(
                baseline_imports = self.get_baseline_imports(),
                custom_imports=folder.get_dag_python_imports(),
                dag_id=folder.get_attribute("FOLDER_NAME"),
                tasks=tasks,
                dependencies=folder.get_dag_dependencies()
            )
            with open(filename, mode="w", encoding="utf-8") as dag_file:
                dag_file.write(content)

        return
    
    def set_baseline_imports(self):
        self.baseline_imports = [
            "from airflow import DAG",
            "from airflow.decorators import task",
        ]
        return
    

    def get_baseline_imports(self):
        return self.baseline_imports



def airflow_task_build(task, template):
    # Load the Template Output Structure
    if template["structure"] is None:
        raise ValueError(
            f"AirShip: no output structure in template: {template['metadata']['name']}, conversion will perform no action")

    if template["mappings"] is None:
        raise ValueError(
            f"AirShip: no mappings in template: {template['metadata']['name']}, conversion will perform no action")

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
        if len(rules) == 0:
            print("No Rules applied to source during mapping")
        for rule in rules:
            print(f"Apply Rule {rule}")
        
        if targetValue is None:
            # TODO - Log That we are going to use the defaults
            targetValue = mapping.get("default", None)
        if targetValue is None:
            # TODO - Log No Default Found, Handle with !UNKNOWN!!
            targetValue = "!!UNKNOWN!!"
        # Construct Values for Output!
        values[targetKey] = targetValue

    # Construct Output Python Object Text
    output = template["structure"].format(**values)
    return output

def airflow_task_python_imports_build(task, template):
    # Load the Template Output Structure
    if template["target"] is None:
        raise ValueError(
            f"AirShip: no target data in template: {template['metadata']['name']}, python imports can not be calculated")
    if template["target"]['operator'] is None:
        raise ValueError(
            f"AirShip: no target operator data in template: {template['metadata']['name']}, python imports can not be calculated")
    if template["target"]['operator']['imports'] is None:
        raise ValueError(
            f"AirShip: no target operator import data in template: {template['metadata']['name']}, python imports can not be calculated")

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
