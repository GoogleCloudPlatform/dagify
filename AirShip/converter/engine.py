import os
import yaml
import xml.etree.ElementTree as ET
from .utils import file_exists, create_directory, directory_extist, is_directory, read_yaml_to_dict, display_dict
from .uf import UF, UFFolder, UFTask, UFTaskVariable, UFTaskInCondition, UFTaskOutCondition, UFTaskShout, base_apply


class Engine():
    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
    ):
        self.DAGs = []

        self.templates = {}
        self.templates_count = 0
        self.templates_path = templates_path
        self.config = {}
        self.config_file = config_file
        self.source_path = source_path
        self.output_path = output_path

        # Run the Proccess
        self.load_config()
        self.load_templates()
        self.load_source()
        self.validate()
        # self.calc_dependencies()
        # self.convert()
        self.convertV2()
        self.generate_airflow_dags()

    def load_config(self):
        print(self.config_file)
        print(os.getcwd())
        print(os.listdir())
        # Validate Template Path Provided
        if self.config_file is None:
            raise ValueError("AirShip: config file not provided")
        if file_exists(self.config_file) is False:
            raise FileNotFoundError("AirShip: conifg file does not exist")

        with open(self.config_file) as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise

        if self.config is None:
            raise ValueError("AirShip: No configuration has been loaded")

        if self.config["config"]["mappings"] is None:
            raise ValueError(
                "AirShip: Configuration loaded with error, no Operator/JobType Mappings loaded")

        # Modify Configration for Standardization:
        for idx, config in enumerate(self.config["config"]["mappings"]):
            # Set Command Uppercase
            self.config["config"]["mappings"][idx]["job_type"] = self.config["config"]["mappings"][idx]["job_type"].upper()
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

    def get_template(self, jobType):
        # validate that Job Type is not Null
        if jobType is None or jobType == "":
            raise ValueError("AirShip: jobType cannot be None or Empty")
        # validate that configuration contains a mapping for job type
        if self.templates.get("jobType", None) is None:
            raise ValueError(
                "AirShip: config file contains no mapping for jobType: {}".format(jobType))
        # return the template for the job type
        return self.templates.get("jobType", None)

    def load_source(self):
        # Read the Source File
        # Parse into AirShip Universial Format
        # Output the AirShip Universial Format Back to the Class
        self.universal_format = None
        if self.source_path is None:
            raise ValueError("AirShip: source file cannot be None or Empty")
        if file_exists(self.source_path) is False:
            raise FileNotFoundError("AirShip: source file not found at {}".format(self.source_path))

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

    def parse(self, root_node):
        uf = {}
        for folder in root_node:
            match folder.tag:
                case "FOLDER" | "SMART_FOLDER":
                    uf[folder.get("FOLDER_NAME")] = {
                        "jobs": {},
                    }

            for job in folder:
                match job.tag:
                    case "JOB":
                        vars = {}
                        incons = []
                        outcons = []
                        shouts = []
                        for item in job:
                            match item.tag:
                                # Construct Variables for Job
                                case "VARIABLE":
                                    vars[item.get("NAME")] = {
                                        "name": item.get("NAME"),
                                        "value": item.get("VALUE"),
                                    }
                                # Construct In Conditions for Job
                                case "INCOND":
                                    incons.append({
                                        "name": item.get("NAME"),
                                        "odate": item.get("ODATE"),
                                        "and_or": item.get("AND_OR"),
                                    })
                                # Construct In Conditions for Job
                                case "OUTCOND":
                                    outcons.append({
                                        "name": item.get("NAME"),
                                        "odate": item.get("ODATE"),
                                        "sign": item.get("SIGN"),
                                    })
                                # Construct Shouts for Job
                                case "SHOUT":
                                    shouts.append({
                                        "when": item.get("WHEN"),
                                        "urgency": item.get("URGENCY"),
                                        "dest": item.get("DEST"),
                                        "message": item.get("MESSAGE"),
                                    })
                                case _:
                                    # TODO Catch this output as unsupported
                                    print(
                                        f"Node type: {item.tag} is not supported for job {job.get('JOBNAME')}")

                        # Construct Job Object
                        uf[folder.get("FOLDER_NAME")]["jobs"][job.get("JOBNAME")] = {
                            "job_name": job.get("JOBNAME"),
                            "description": job.get("DESCRIPTION"),
                            "job_isn": job.get("JOBISN"),
                            "application": job.get("APPLICATION"),
                            "sub_application": job.get("SUB_APPLICATION"),
                            "memname": job.get("MEMNAME"),
                            "created_by": job.get("CREATED_BY"),
                            "run_as": job.get("RUN_AS"),
                            "priority": job.get("PRIORITY"),
                            "critical": job.get("CRITICAL"),
                            "task_type": job.get("TASKTYPE"),
                            "cyclic": job.get("CYCLIC"),
                            "node_id": job.get("NODEID"),
                            "interval": job.get("INTERVAL"),
                            "cmd_line": job.get("CMDLINE"),
                            "confirm": job.get("CONFIRM"),
                            "retro": job.get("RETRO"),
                            "maxwait": job.get("MAXWAIT"),
                            "maxrerun": job.get("MAXRERUN"),
                            "autoarch": job.get("AUTOARCH"),
                            "maxdays": job.get("MAXDAYS"),
                            "maxruns": job.get("MAXRUNS"),
                            "timefrom": job.get("TIMEFROM"),
                            "weekdays": job.get("WEEKDAYS"),
                            "jan": job.get("JAN"),
                            "feb": job.get("FEB"),
                            "mar": job.get("MAR"),
                            "apr": job.get("APR"),
                            "may": job.get("MAY"),
                            "jun": job.get("JUN"),
                            "jul": job.get("JUL"),
                            "aug": job.get("AUG"),
                            "sep": job.get("SEP"),
                            "oct": job.get("OCT"),
                            "nov": job.get("NOV"),
                            "dec": job.get("DEC"),
                            "days_and_or": job.get("DAYS_AND_OR"),
                            "shift": job.get("SHIFT"),
                            "shiftnum": job.get("SHIFTNUM"),
                            "sysdb": job.get("SYSDB"),
                            "jobs_in_group": job.get("JOBS_IN_GROUP"),
                            "ind_cyclic": job.get("IND_CYCLIC"),
                            "creation_user": job.get("CREATION_USER"),
                            "creation_date": job.get("CREATION_DATE"),
                            "creation_time": job.get("CREATION_TIME"),
                            "change_userid": job.get("CHANGE_USERID"),
                            "change_date": job.get("CHANGE_DATE"),
                            "change_time": job.get("CHANGE_TIME"),
                            "rule_based_calendar_relationship": job.get(
                                "RULE_BASED_CALENDAR_RELATIONSHIP"),
                            "appl_type": job.get("APPL_TYPE"),
                            "multy_agent": job.get("MULTY_AGENT"),
                            "use_instream_jcl": job.get("USE_INSTREAM_JCL"),
                            "version_serial": job.get("VERSION_SERIAL"),
                            "version_host": job.get("VERSION_HOST"),
                            "cyclic_tolerance": job.get("CYCLIC_TOLERANCE"),
                            "cyclic_type": job.get("CYCLIC_TYPE"),
                            "parent_folder": job.get("PARENT_FOLDER"),
                            "variables": vars,
                            "in_conditions": incons,
                            "out_conditions": outcons,
                            "shouts": shouts,
                            "JOB_DEPS": [],
                            "JOB_RAW": str(job)
                        }
        return uf

    def calc_dependencies(self):
        return

    def convertV2(self):
        if self.uf is None:
            raise ValueError(
                f"AirShip: no data in universal format. nothing to convert!")

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
                print(f" --> Converting Job number {str(tIdx)}: {task_name}, \n \
 \t from Source Platform {src_platform_name} to Target Platform: {tgt_platform_name}\n \
 \t from Source Operator {src_operator_name} to Target Operator: {tgt_operator_name}\n \
 \t with template: {template_name}\n")

                output = airflow_task_buildV2(task, template)
                imports = airflow_imports_buildV2(task, template)
                task.set_output_airflow_task(output)


    def convert(self):

        folder_count = 0
        job_count = 0

        if self.universal_format is None:
            raise ValueError(
                f"AirShip: no data in universal format. nothing to convert!")

        # Iterate folders
        for folder in self.universal_format:
            folder_count += 1
            # Iterate jobs
            for item in self.universal_format[folder]["jobs"]:
                job = self.universal_format[folder]["jobs"][item]
                job_count += 1
                # Process each job
                # determine job type:
                job_type = job.get("task_type", None)
                job_name = job.get("job_name", "UNKNOWN_JOB_NAME")
                if job_type is None:
                    raise ValueError(
                        f"AirShip: no task/job_type in source for job: {job_name}")
                # get the template name from config.yaml based on job_type
                # TODO Add filter support
                template_name = self.get_template_name(job_type)
                # get the template from the template name
                template = self.get_template(template_name)
                if template is None:
                    raise ValueError(
                        f"AirShip: no template name provided that matches job type {job_type}")

                # work out the mappings from the template;

                # Access Job Details:
                src_platform_name = template["source"]["platform"].get(
                    "name", "UNKNOWN_SOURCE_PLATFORM")
                src_operator_name = template["source"]["operator"].get(
                    "id", "UNKNOWN_SOURCE_PLATFORM")
                tgt_platform_name = template["target"]["platform"].get(
                    "name", "UNKNOWN_TARGET_PLATFORM")
                tgt_operator_name = template["target"]["operator"].get(
                    "name", "UNKNOWN_TARGET_PLATFORM")
                # print(f" --> Converting Job number {str(job_count)}: {job_name}, \n \
# \t from Source Platform {src_platform_name} to Target Platform: {tgt_platform_name}\n \
# \t from Source Operator {src_operator_name} to Target Operator: {tgt_operator_name}\n \
# \t with template: {template_name}\n")

                # Construct Airflow Task from Job and Template
                output = airflow_task_build(job, template)
                if output is None:
                    # TODO Log Error Constructing DAG Task
                    continue

                # print(output)

        return

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
            raise ValueError(
                f"AirShip: no data in universal format. nothing to convert!")

        imports = []
        dag_id = ""
        tasks = []
        dependencies = []

        # process the conversion of all universal format items
        for fIdx, folder in enumerate(self.uf.get_folders()):
            # process a single folder
            for tIdx, task in enumerate(folder.get_tasks()):
                # Capture the airflow tasks
                tasks.append(task.get_output_airflow_task())
                # Capture the airflow task imports
                # tasks.append(task.get_output_airflow_task())

         # Get DAG Template
        # environment = Environment(loader=FileSystemLoader("./converter/templates/"))
        # template = environment.get_template("dag.tmpl")

        outputDir = self.output_path
        # if directory_extist(outputDir) is False:
        #    create_directory(outputDir)

        # Create DAG File by Folder
        # filename = f"output/{folder.get_folder_name()}.py"
        # content = template.render(
        #    imports=folder.calculate_imports(),
        #    dag_id=folder.get_folder_name_safe(),
        #    tasks=folder.get_jobs_operator_as_string_list(),
        #    dependencies=folder.calculate_job_dependencies()
        # )
        # with open(filename, mode="w", encoding="utf-8") as dag_file:
        #    dag_file.write(content)

        return


"""
    Read the Universal Format
    -->> Loop the Folders
    -->> Loop the Jobs
        --> GET the Config Mapping (Template) based on the Job Source Type;
                [

                ]
        --> Read the Template Object from The Loaded Templates;
        --> Map the Field from Source -> Target Using the Template
        --> Store the Python Task Def
        --> Store the YAML Task Def ()
        --> Store the Reporting Metrics and Findings for this Job.
    -->> Process Jobs and Build Dependencies
        --> Store Dependencies
    --> Construct DAG from all Stored Jobs
    --> Construct Report from all Stored Jobs Findings
    --> Construct YAML Output  from all Stored Jobs for "Dag Builder"
    --> Output all Files Created
"""


def airflow_imports_buildV2(task, template):
    if template["target"] is None:
        raise ValueError(
            f"AirShip: no target in template: {template['metadata']['name']}, python import statements will be missing")
    if template["target"]["operator"] is None:
        raise ValueError(
            f"AirShip: no target operstor listed in template: {template['metadata']['name']}, python import statements will be missing")
    if template["target"]["operator"]["imports"] is None:
        raise ValueError(
            f"AirShip: no imports listed in template: {template['metadata']['name']}, python import statements will be missing")

    imports = []
    for imp in template["target"]["operator"]["imports"]:
        for package in imp.get("packages", []):
            imports.append(f"from {package} import {imp['module']}")

    return


def airflow_task_buildV2(task, template):
    # Load the Template Output Structure
    output = template["structure"]
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
        if targetValue is None:
            # TODO - Log That we are going to use the defaults
            targetValue = mapping.get("default", None)
        if targetValue is None:
            # TODO - Log No Default Found, Handle with !UNKNOWN!!
            targetValue = "!!UNKNOWN!!"
        # Construct Values for Output!
        values[targetKey] = targetValue

    # Construct Output Python Object Text
    output = output.format(**values)
    return output


def airflow_task_build(job, template):

    # Load the Template Output Structure
    output = template["structure"]
    if template["structure"] is None:
        raise ValueError(
            f"AirShip: no output structure in template: {template['metadata']['name']}, conversion will perform no action")
        return None

    if template["mappings"] is None:
        raise ValueError(
            f"AirShip: no mappings in template: {template['metadata']['name']}, conversion will perform no action")
        return None

    # Declare Output Values Dictionary
    values = {}

    # Process each Mapping
    for mapping in template["mappings"]:
        # Lookup Mapping Target Key
        targetKey = mapping.get('target', None)
        if targetKey is None:
            # If Key is None, Skip
            continue

        # Load Target Value or Default Value for TargetKey from Job Source
        # Field
        targetValue = job.get(
            mapping["source"], job.get(
                mapping.get("default"), None))
        if targetValue is None:
            # No Value Found and No Default; Skip this mapping.
            # TODO Log Error Value Output (Required to Prevent String
            # Formatting Failure)
            targetValue = "!!UNKNOWN!!"

        # Construct Values for Output!
        values[targetKey] = targetValue

    # Construct Output Python Object Text
    output = output.format(**values)
    return output
