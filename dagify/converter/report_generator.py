"""Module providing function to manipulate yaml files"""
import yaml
from .utils import (
    is_directory,
    generate_report,
    get_jobtypes_andcount,
    generate_json,
    format_table_data
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
        self.output_path = output_path
        self.templates_path = templates_path

        # Run the Proccess
        self.generate_report()

    def generate_report(self):
        """Function that generates the json and txt report"""
        templates_to_validate = []
        ##Config_File_Info parameters 
        config_job_types = []
        config_job_types_count = 0
        ## Source_file_Info parameters
        source_files_count = 1
        source_file_info = []
        job_types_source= []
        job_types_source_count = 0

        ## Get the Job_types from config_file
        config_job_types, config_job_types_count = get_jobtypes_andcount(self.config_file)


        ## Get the Job_types from source xml
        if is_directory(self.source_path) is False:
            source_file_info.append(self.source_path.split("/")[-1])
            job_types_source, job_types_source_count = get_jobtypes_andcount(self.source_path)

        ### Get templates INFO
        with open(self.config_file, encoding="utf-8") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc
        for idx,config in enumerate(self.config["config"]["mappings"]):
            # Set Command Uppercase
            self.config["config"]["mappings"][idx]["job_type"] = \
                self.config["config"]["mappings"][idx]["job_type"].upper()
            templates_to_validate.append(self.config["config"]["mappings"][idx]["template_name"])


        ## Statistics Info parameters 
        job_types_converted,job_types_not_converted,converted_percentage, \
            non_converted_percentage = \
            self.get_statistics(job_types_source,config_job_types)
        ## Table Info
        statistics= [
            f"Percentage of Jobtypes converted: {converted_percentage}%", 
            f"Percentage of Jobtypes not converted: {non_converted_percentage}%"
            ]
        title = "DAGIFY REPORT"
        columns = ["TASK","INFO","COUNT"]
        rows = [
                ["Source_files", source_file_info, source_files_count],
                ["Source_File_Job_Types", job_types_source, job_types_source_count],
                ["Config_File_Job_Types", config_job_types, config_job_types_count],
                ["Job_Types_Converted",job_types_converted,len(job_types_converted)],
                ["Job_types_Not_Converted",job_types_not_converted,len(job_types_not_converted)],
                ["Templates_validated", templates_to_validate, len(templates_to_validate)]
        ]
        formatted_table_data = format_table_data(title,columns,rows)

        warning_line = "NOTE: If the job_type \
            is not defined in the config.yaml or \
            if the job_type does not have a matching template defined, \
            it would be by default converted into a DUMMYOPERATOR"

        generate_json(statistics,formatted_table_data,self.output_path)
        generate_report(statistics,title, columns, rows, warning_line,self.output_path)

    def get_statistics(self,source_jt, config_jt):
        """Function to caluculate the percentage conversion"""
        converted_percent = 0
        non_converted_percent = 0

        ## Conversion Info
        job_types_converted = list(set(config_jt) & set(source_jt))
        job_types_not_converted = list(set(source_jt) - set(config_jt))

        ## Percentages
        non_converted_percent = (len(job_types_not_converted)/len(source_jt))*100 
        converted_percent = 100 - non_converted_percent

        return job_types_converted,job_types_not_converted,converted_percent,non_converted_percent
