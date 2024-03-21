import os
import yaml
import xml.etree.ElementTree as ET
from .utils import file_exists, create_directory, directory_extist, is_directory, read_yaml_to_dict, display_dict


class Logging():
    def __init__(self, debug=False):
        self.debug = debug
        self.trace = []
        self.warnings = []
        self.errors = []
        self.info = []
        self.debug = []

    def addTrace(self, item):
        # stoe all items as a trace item
        self.trace.append(item)
        # if debug mode output every trace in realtime.
        if self.debug:
            print(item)

    def trace_count(self):
        return len(self.trace)

    def addWarn(self, item):
        # trace all warnings
        self.addTrace(item)
        # store all warnings
        self.warnings.append(item)

    def warn_count(self):
        return len(self.warn)

    def addError(self, item):
        # trace all errors
        self.addTrace(item)
        # store all errors
        self.errors.append(item)

    def error_count(self):
        return len(self.error)

    def addInfo(self, item):
        # trace all info messages
        self.addTrace(item)
        # store all info messages
        self.info.append(item)

    def info_count(self):
        return len(self.info)

    def addDebug(self, item):
        # trace all debug messages
        self.addTrace(item)
        # store all debug messages
        self.debug.append(item)

    def debug_count(self):
        return len(self.debug)



class Engine():
    def __init__(self, templates_path="./templates", config_path="./config.yaml", source_file=None):
        self.log = Logging()
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
        self.calc_dependencies()
        self.validate_config()
        #self.convert()

    def load_config(self):
        # Validate Template Path Provided
        if self.config_path is None:
            raise ValueError("AirShip: config file path not provided")
        if file_exists(self.config_path) is False:
            raise FileNotFoundError("AirShip: conifg path does not exist")
    
        with open(self.config_path) as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise
        return

    def validate_config(self):
        
        to_validate = self.get_distinct_job_types()
        for mapping in to_validate:
            print(mapping)
            if mapping.upper() not in self.config["config"]["mappings"]:
                raise Exception(f"AirShip: source file contains job type {mapping.upper()}; No template mapping has been provided in the config for this job type.")
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

        self.log.addInfo("AirShip: {} templates loaded".format(self.templates_count))
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
                                "JOB_DEPS": []
                        }
        return uf

    def calc_dependencies(self): 
        return

    def convert(self):
        
        #Iterate folders
        for folder in self.universal_format:
            # Iterate jobs
            for job in self.universal_format[folder]["jobs"]:
                # Process each job
                # determine job type:
                job_type = self.universal_format[folder]["jobs"][job]["task_type"]
                # get the template name from config.yaml based on job_type
                template_filename = self.get_job_type_template_filename(job_type)
                # get the template from the template name
                template = self.get_template(template_filename)
                
                # work out the mappings from the template;
                
        return

    def get_template(self, template_filename):    
        # Validate template_name is Provided
        #if template_name is None:
        #    raise ValueError("AirShip: template name must be provided")
        #if file_exists(self.template_path) is False:
        #    raise FileNotFoundError("AirShip: named template  ")
    
        #with open(self.config_path) as stream:
        #    try:
        ##        self.config = yaml.safe_load(stream)
         #   except yaml.YAMLError as exc:
         #       raise
        #return
        
        return    

    def get_job_type_template_filename(self, job_type):
        for command in self.config["config"]["mappings"]:
                # Look for a job_type match. 
                if command["job_type"].upper() == job_type.upper():
                    return command["template_filename"]        
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
