from jinja2 import Environment, FileSystemLoader
from .exceptions import InvalidConverterType, DisabledConverterType
from .utils import clean_converter_type
from .config import Config
from .utils import file_exists, clean_converter_type, create_directory, directory_extist

# ControlM Imports
import xml.etree.ElementTree as ET
from .platform.controlm import Workflow, Folder, Job, InCondition, OutCondition, Shout, Variable,  BaseOperator, SSHOperator, DummyOperator, UnknownOperator

def new_converter(converter_type=None):
    try:
        # ensure converter type is passed
        if converter_type is None:
            raise InvalidConverterType(f"converter type must be provided, detected NoneType")
        # clean the converter_type variable to reduce errors
        converter_type = clean_converter_type(converter_type)
        # look Up converter configuration
        selected = Config().getConverters().get(converter_type.upper(), None)
        # validate if converter_type is valid
        if selected is None:
            raise InvalidConverterType(f"unsupported converter type: {converter_type}")
        # validate if converter_type is enabled
        if selected["enabled"] is False:
            raise DisabledConverterType(f"converter type: {converter_type} is currently disabled or under development")
        # return correct converter class
        match selected.get("id", None).upper():
            case "CONTROLM":
                # return ControlMConverter() class
                return ControlMConverter()
            case _:
                # raise exception
                raise InvalidConverterType(f"unsupported converter type: {converter_type}")

    except (InvalidConverterType, DisabledConverterType) as e:
        return None


class AirShipConverter():
    def __init__(self, converter=None):
        pass


class ControlMConverter(AirShipConverter):
    def __init__(self):
        pass
    

    def analyze(sself, xml_path=None):
        if xml_path is None:
            raise Exception("Analysis: XML Path must be provided")
        if file_exists(xml_path) is False:
            raise Exception("Analysis: XML File does not exist at path provided")
        pass

    def parse(self, xml_path=None):
        if xml_path is None:
            raise Exception("Parser: XML Path must be provided")
        if file_exists(xml_path) is False:
            raise Exception("Parser: XML File does not exist at path provided")


        self.xml_path = xml_path
        # TODO: Use Utility Function to confirm file exists at path.
        #      on error raise exception.

        tree = ET.parse(self.xml_path)
        root = tree.getroot()

        workflow = Workflow(
            filename=self.xml_path
        )

        # Parse the XML File
        workflow = _parse_struct(root, workflow)
        workflow = _convert_operators(workflow)
        _create_dag_files(workflow)

        return


def _parse_struct(root_node, parent):
    for node in root_node:
        match node.tag:
            case "FOLDER" | "SMART_FOLDER":
                folder = Folder(
                    datacenter=node.get("DATACENTER"),
                    version=node.get("VERSION"),
                    platform=node.get("PLATFORM"),
                    folder_name=node.get("FOLDER_NAME"),
                    modified=node.get("MODIFIED"),
                    last_upload=node.get("LAST_UPLOAD"),
                    folder_order_method=node.get("FOLDER_ORDER_METHOD"),
                    real_folder_id=node.get("REAL_FOLDER_ID"),
                    type=node.get("TYPE"),
                    used_by_code=node.get("USED_BY_CODE"),
                )
                parent.add_folder(folder)
                _parse_struct(node, folder)

            case "JOB":
                job = Job(
                    job_name=node.get("JOBNAME"),
                    description=node.get("DESCRIPTION"),
                    jobISN=node.get("JOBISN"),
                    application=node.get("APPLICATION"),
                    sub_application=node.get("SUB_APPLICATION"),
                    memname=node.get("MEMNAME"),
                    created_by=node.get("CREATED_BY"),
                    run_as=node.get("RUN_AS"),
                    priority=node.get("PRIORITY"),
                    critical=node.get("CRITICAL"),
                    tasktype=node.get("TASKTYPE"),
                    cyclic=node.get("CYCLIC"),
                    node_id=node.get("NODEID"),
                    interval=node.get("INTERVAL"),
                    cmd_line=node.get("CMDLINE"),
                    confirm=node.get("CONFIRM"),
                    retro=node.get("RETRO"),
                    maxwait=node.get("MAXWAIT"),
                    maxrerun=node.get("MAXRERUN"),
                    autoarch=node.get("AUTOARCH"),
                    maxdays=node.get("MAXDAYS"),
                    maxruns=node.get("MAXRUNS"),
                    timefrom=node.get("TIMEFROM"),
                    weekdays=node.get("WEEKDAYS"),
                    jan=node.get("JAN"),
                    feb=node.get("FEB"),
                    mar=node.get("MAR"),
                    apr=node.get("APR"),
                    may=node.get("MAY"),
                    jun=node.get("JUN"),
                    jul=node.get("JUL"),
                    aug=node.get("AUG"),
                    sep=node.get("SEP"),
                    oct=node.get("OCT"),
                    nov=node.get("NOV"),
                    dec=node.get("DEC"),
                    days_and_or=node.get("DAYS_AND_OR"),
                    shift=node.get("SHIFT"),
                    shiftnum=node.get("SHIFTNUM"),
                    sysdb=node.get("SYSDB"),
                    jobs_in_group=node.get("JOBS_IN_GROUP"),
                    ind_cyclic=node.get("IND_CYCLIC"),
                    creation_user=node.get("CREATION_USER"),
                    creation_date=node.get("CREATION_DATE"),
                    creation_time=node.get("CREATION_TIME"),
                    change_userid=node.get("CHANGE_USERID"),
                    change_date=node.get("CHANGE_DATE"),
                    change_time=node.get("CHANGE_TIME"),
                    rule_based_calendar_relationship=node.get(
                        "RULE_BASED_CALENDAR_RELATIONSHIP"),
                    appl_type=node.get("APPL_TYPE"),
                    multy_agent=node.get("MULTY_AGENT"),
                    use_instream_jcl=node.get("USE_INSTREAM_JCL"),
                    version_opcode=node.get("VERSION_OPCODE"),
                    is_current_version=node.get("IS_CURRENT_VERSION"),
                    version_serial=node.get("VERSION_SERIAL"),
                    version_host=node.get("VERSION_HOST"),
                    cyclic_tolerance=node.get("CYCLIC_TOLERANCE"),
                    cyclic_type=node.get("CYCLIC_TYPE"),
                    parent_folder=node.get("PARENT_FOLDER"),
                )
                parent.add_job(job)
                _parse_struct(node, job)

            case "VARIABLE":
                var = Variable(
                    name=node.get("NAME"),
                    value=node.get("VALUE"),
                )
                parent.add_variable(var)
                _parse_struct(node, var)

            case "INCOND":
                var = InCondition(
                    name=node.get("NAME"),
                    odate=node.get("ODATE"),
                    and_or=node.get("AND_OR"),
                )
                parent.add_in_condition(var)
                _parse_struct(node, var)

            case "OUTCOND":
                var = OutCondition(
                    name=node.get("NAME"),
                    odate=node.get("ODATE"),
                    sign=node.get("SIGN"),
                )
                parent.add_out_condition(var)
                _parse_struct(node, var)

            case "SHOUT":
                var = Shout(
                    when=node.get("WHEN"),
                    urgency=node.get("URGENCY"),
                    dest=node.get("DEST"),
                    message=node.get("MESSAGE")
                )
                parent.add_shout(var)
                _parse_struct(node, var)
            case _:
                print("Node: " + node.tag + " is not currently supported.")

    return parent




def _convert_operators(workflow):
    for folder in workflow.get_folders():
        for job in folder.get_jobs():
            # Create Airflow Operator Object
            op = None
            match job.get_job_type():
                case "Command":
                    # -- Mapping ---
                    # Control-M JobType: Command
                    # Airflow Operator: SSHOperator
                    op = SSHOperator(
                        task_id=job.get_job_name_safe(),
                        command=job.get_cmd_line_safe(),
                    )
                case "Dummy":
                    # -- Mapping ---
                    # Control-M JobType: Dummy
                    # Airflow Operator: DummyOperator
                    op = DummyOperator(
                        task_id=job.get_job_name_safe(),
                    )
                case _:
                    # -- Mapping ---
                    # Control-M JobType: ????
                    # Airflow Operator: ????
                    print(
                        "Job Type: " + job.get_job_type() +
                        " for job: " + job.get_job_name() +
                        " is not currently supported.")
                    op = UnknownOperator()

            # Set Job Operator
            job.set_operator(op)

    return workflow


def _create_dag_files(workflow):
    # Process Dag Output files
    for folder in workflow.get_folders():
        # Get DAG Template
        print("hi..")
        environment = Environment(loader=FileSystemLoader("./converter/templates/"))
        template = environment.get_template("dag.tmpl")
        
        outputDir = "./output"
        if directory_extist(outputDir) is False: 
            create_directory(outputDir)
        
        # Create DAG File by Folder
        filename = f"output/{folder.get_folder_name()}.py"
        content = template.render(
            imports=folder.calculate_imports(),
            dag_id=folder.get_folder_name_safe(),
            tasks=folder.get_jobs_operator_as_string_list(),
            dependencies=folder.calculate_job_dependencies()
        )
        with open(filename, mode="w", encoding="utf-8") as dag_file:
            dag_file.write(content)