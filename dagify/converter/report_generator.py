"""Module providing function to manipulate yaml files"""
import xml.etree.ElementTree as ET
import yaml

from .uf import (
    UF,
    UFTask,
    UFTaskVariable,
    UFTaskInCondition,
    UFTaskOutCondition,
    UFTaskShout,
)

from .utils import (
    file_exists,
    is_directory,
    generate_report_utils,
    get_jobtypes_andcount,
    generate_json,
    format_table_json,
    get_job_info,
    get_tasktype_statistics,
    get_job_statistics,
    filter_jobs_by_parameter_in_child,
    calculate_cron_schedule,
    directory_exists,
    create_directory,
    generate_table
)


class Report():
    """Report generating module """

    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
    ):
        self.config_file = config_file
        self.config = {}
        self.templates = {}
        self.source_path = source_path
        source_xml_name = self.source_path.split("/")[-1].split(".")[0]
        self.output_path = f"{output_path}/{source_xml_name}"
        self.templates_path = templates_path

        # Run the Proccess
        self.load_source()
        self.write_report()

    def load_source(self):
        """ Read the Source File
            Parse into dagify Universial Format
            Output the dagify Universial Format Back to the Class"""
        self.universal_format = None
        if self.source_path is None:
            raise ValueError("dagify: source file cannot be None or Empty")
        if file_exists(self.source_path) is False:
            raise FileNotFoundError(
                "dagify: source file not found at {}".format(
                    self.source_path))

        root = ET.parse(self.source_path).getroot()
        self.uf = self.parse_universal_format(root)
        return

    def parse_universal_format(self, source):
        """Function to parse uf"""
        uf = UF()
        uf = self.parse_controlm_tree(source, uf)
        return uf

    def parse_controlm_tree(self, root_node, parent):
        """Function to parse control m"""
        for node in root_node:
            match node.tag:
                case "FOLDER" | "SMART_FOLDER":
                    # ufFolder = UFFolder()
                    # ufFolder.from_controlm_xml(node)
                    # parent.add_folder(ufFolder)
                    self.parse_controlm_tree(node, parent)
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

    def check_schedules(self, xml_file_path, dag_divider):
        """Function to check schedules exist and generate reprot table"""
        title = "Updated Job Schedules"
        columns = ["JOB NAME", "DAG DIVIDER", "SCHEDULE CHANGE", "ORIGINAL SCHEDULE", "DAG SCHEDULE"]
        rows = []
        prev_divider = None
        dag_schedule = None

        universal_format = self.uf
        tasks = universal_format.get_tasks()
        for tIdx, task in enumerate(tasks):
            current_divider = task.get_attribute(dag_divider)

            if not prev_divider:
                prev_divider = current_divider

            if prev_divider and prev_divider != current_divider:  # New DAG and schedule will be created
                prev_divider = current_divider
                dag_schedule = None  # reset schedule to empty

            if not dag_schedule:  # first schedule for this dag , defined for all jobs with this divider
                dag_schedule = calculate_cron_schedule(task)
                if not dag_schedule:
                    dag_schedule = "@daily"

            if current_divider == prev_divider:
                current_schedule = calculate_cron_schedule(task)
                job_name = task.get_attribute("JOBNAME")
                if current_schedule != dag_schedule:

                    rows.append((job_name, current_divider, "YES", current_schedule, dag_schedule))
                else:
                    rows.append((job_name, current_divider, "NO", current_schedule, dag_schedule))

        return title, columns, rows

    def generate_report(self):
        """Function that generates the json and txt report"""
        templates_to_validate = []
        # Config_File_Info parameters
        config_job_types = []
        config_job_types_count = 0
        # Source_file_Info parameters
        source_files_count = 1
        source_file_info = []
        job_types_source = []
        job_types_source_count = 0

        # Get the Job_types from config_file
        config_job_types, config_job_types_count = get_jobtypes_andcount(self.config_file)

        # Get the Job_types from source xml
        if is_directory(self.source_path) is False:
            source_file_info.append(self.source_path.split("/")[-1])
            job_types_source, job_types_source_count = get_jobtypes_andcount(self.source_path)

        # Get templates INFO
        with open(self.config_file, encoding="utf-8") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc
        for idx, config in enumerate(self.config["config"]["mappings"]):
            self.config["config"]["mappings"][idx]["job_type"] = \
                self.config["config"]["mappings"][idx]["job_type"].upper()
            templates_to_validate.append(self.config["config"]["mappings"][idx]["template_name"])

        # Get job related info
        job_info = get_job_info(self.source_path)
        unconverted_job_name, converted_job_name, \
            non_converted_job_percent, converted_job_percent,conv_job_count = \
            get_job_statistics(job_info, config_job_types)
        # Statistics Info parameters
        job_types_converted, job_types_not_converted, converted_percentage, \
            non_converted_percentage = \
            get_tasktype_statistics(job_types_source, config_job_types)
        # Get Manual Intervention Job_Name Info
        manual_job_names = filter_jobs_by_parameter_in_child(self.source_path, "CONFIRM")

        # Table Info
        statistics = [
            f"Jobtypes converted: {len(job_types_converted)}/{len(job_types_source)}",
            f"Percentage of Jobtypes converted: {converted_percentage}%",
            f"Percentage of Jobtypes not converted: {non_converted_percentage}%",
            f"Jobs converted: {conv_job_count}/{len(job_info)}",
            f"Percentage of Jobs converted: {converted_job_percent}%",
            f"Percentage of Jobs not converted: {non_converted_job_percent}%",
        ]
        title = "DAGIFY REPORT"
        columns = ["TASK", "INFO", "COUNT"]
        rows = [
            ["Source_files", source_file_info, source_files_count],
            ["Source_File_Job_Types", job_types_source, job_types_source_count],
            ["Config_File_Job_Types", config_job_types, config_job_types_count],
            ["Job_Types_Converted", job_types_converted, len(job_types_converted)],
            ["Job_types_Not_Converted", job_types_not_converted, len(job_types_not_converted)],
            ["Jobs_Converted", converted_job_name, len(converted_job_name)],
            ["Jobs_Not_Converted", unconverted_job_name, len(unconverted_job_name)],
            ["Jobs_Requiring_Manual_Approval", manual_job_names, len(manual_job_names)],
            ["Templates_Validated", templates_to_validate, len(templates_to_validate)]
        ]
        #formatted_table_data = format_table_json(title, columns, rows)

        # Writes out JSON
        #generate_json(statistics, formatted_table_data, self.output_path)

        warning_line = "NOTE: \n \
        1. If the job_type is not defined in the config.yaml or if the job_type does not have a matching template defined,it would be by default converted into a DUMMYOPERATOR\n \
        2. Jobs_Requiring_Manual_Approval - indicates that the job has CONFIRM PARAMTER defined in job, meaning the workflow has to be changed for manual approval for these jobs/job"

        return title, columns, rows, statistics, warning_line

    def write_report(self):
        """Function that generates the json and txt report"""
        report_tables = []
        if not directory_exists(self.output_path):
            create_directory(self.output_path)
            # clear_directory(self.output_path)

        job_title, job_columns, job_rows, job_statistics, job_warning = self.generate_report()
        job_conversion_table = generate_table(job_title, job_columns, job_rows)

        schedules_title, schedules_columns, schedules_rows = self.check_schedules(self.source_path, dag_divider="PARENT_FOLDER")
        schedule_table = generate_table(schedules_title, schedules_columns, schedules_rows)

        report_tables.append(job_conversion_table)
        report_tables.append(schedule_table)
        generate_report_utils(report_tables, self.output_path, job_statistics, job_warning)
        #json_generation
        formatted_job_table_data = format_table_json(job_title, job_columns, job_rows)
        formatted_schedule_table_data = format_table_json(schedules_title, schedules_columns, schedules_rows)
        generate_json(job_statistics, formatted_job_table_data,formatted_schedule_table_data, self.output_path)
