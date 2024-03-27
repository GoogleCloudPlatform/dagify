import os
import yaml
import xml.etree.ElementTree as ET
from .utils import file_exists, create_directory, directory_extist, is_directory, read_yaml_to_dict, display_dict


class Engine():
    def __init__(self, templates_path="./templates", config_path="./config.yaml", source_file=None):
        self.templates = {}
        self.templates_count = 0
        self.templates_path = templates_path
        self.config = {}
        self.config_path = config_path
        self.source_file = source_file

        # Run the Proccess
        self.load_config()
        self.load_templates()
        self.load_source()
        self.validate()
        self.calc_dependencies()
        self.convert()

    def load_config(self):
        # Validate Template Path Provided
        if self.config_path is None:
            raise ValueError("AirShip: config file path not provided")
        if file_exists(self.config_path) is False:
            raise FileNotFoundError("AirShip: conifg path does not exist")
    
        
        with open(self.config_path) as stream:
            try:
                 self.config =  yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise
        
        if self.config is None:
            raise ValueError("AirShip: No configuration has been loaded") 
        
        if self.config["config"]["mappings"] is None:
            raise ValueError("AirShip: Configuration loaded with error, no Operator/JobType Mappings loaded")
        
        # Modify Configration for Standardization:
        for idx, config in enumerate(self.config["config"]["mappings"]):
            # Set Command Uppercase 
             self.config["config"]["mappings"][idx]["job_type"] = self.config["config"]["mappings"][idx]["job_type"].upper()
        return

    def validate(self):
        # TODO
        # Check that every Job in the Source has a Configured Mapping in Config
        # Check that every JobType in Config has a Template Name and that that Template Name is in Templates;
        
        return

    def load_templates(self):
        # This will load all templates from the provide path into a universal HashMap for Direct Referencing

        # Validate Template Path Provided
        if self.templates_path is None:
            raise ValueError("AirShip: Templates path not provided")
        if is_directory(self.templates_path) is False:
            raise NotADirectoryError("AirShip: Templates path is not a directory")

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
            raise ValueError("AirShip: config file contains no mapping for jobType: {}".format(jobType))
        # return the template for the job type
        return self.templates.get("jobType", None)

    def load_source(self):
        # Read the Source File
        # Parse into AirShip Universial Format
        # Output the AirShip Universial Format Back to the Class
        self.universal_format = None

        if self.source_file is None:
            raise ValueError("AirShip: source file cannot be None or Empty")
        if file_exists(self.source_file) is None:
            raise FileNotFoundError("AirShip: source file not found")


        tree = ET.parse(self.source_file)
        root = tree.getroot()

        self.universal_format = self.parse(root)
        return

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
                                    print(f"Node type: {item.tag} is not supported for job {job.get('JOBNAME')}")

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

    def convert(self):
        
        folder_count = 0
        job_count = 0
        
        #Iterate folders
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
                    raise ValueError(f"AirShip: no task/job_type in source for job: {job_name}")
                # get the template name from config.yaml based on job_type
                # TODO Add filter support
                template_name = self.get_template_name(job_type)
                # get the template from the template name
                template = self.get_template(template_name)
                if template is None: 
                    raise ValueError(f"AirShip: no template name provided that matches job type {job_type}")
                
                # work out the mappings from the template;
                
                # Access Job Details: 
                src_platform_name = template["source"]["platform"].get("name", "UNKNOWN_SOURCE_PLATFORM")
                src_operator_name = template["source"]["operator"].get("id", "UNKNOWN_SOURCE_PLATFORM")
                tgt_platform_name = template["target"]["platform"].get("name", "UNKNOWN_TARGET_PLATFORM")
                tgt_operator_name = template["target"]["operator"].get("name", "UNKNOWN_TARGET_PLATFORM")
                print(f" --> Converting Job number {str(job_count)}: {job_name}, \n \
\t from Source Platform {src_platform_name} to Target Platform: {tgt_platform_name}\n \
\t from Source Operator {src_operator_name} to Target Operator: {tgt_operator_name}\n \
\t with template: {template_name}\n")
                
                # Construct Airflow Task from Job and Template
                output = airflow_task_build(job, template)
                if output is None:
                    #TODO Log Error Constructing DAG Task
                    continue
                
                print(output)
                
                
                
        return

    def get_template(self, template_name):    
        # Validate template_name is Provided
        if template_name is None:
            raise ValueError("AirShip: template name must be provided")        
        template = self.templates.get(template_name, None)
        if template is None:
            raise ValueError(f"AirShip: no template with name: '{template_name}' was not found among loaded templates.")
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
                job_types.append(self.universal_format[folder]["jobs"][job]["task_type"].upper())
        
        # return distinct set of job types
        return list(set(job_types))

       
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




def airflow_task_build(job, template):
    
    # Load the Template Output Structure
    output = template["structure"]
    if template["structure"] is None: 
        raise ValueError(f"AirShip: no output structure in template: {template['metadata']['name']}, conversion will perform no action")
        return None

    if template["mappings"] is None: 
        raise ValueError(f"AirShip: no mappings in template: {template['metadata']['name']}, conversion will perform no action")
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
        
        # Load Target Value or Default Value for TargetKey from Job Source Field
        targetValue = job.get(mapping["source"], job.get(mapping.get("default"), None))
        if targetValue is None: 
            # No Value Found and No Default; Skip this mapping. 
            # TODO Log Error Value Output (Required to Prevent String Formatting Failure)
            targetValue = "!!UNKNOWN!!"

        # Construct Values for Output!
        values[targetKey] = targetValue
    
    # Construct Output Python Object Text
    output = output.format(**values)
    return output