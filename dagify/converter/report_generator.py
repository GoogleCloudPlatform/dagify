import xml.etree.ElementTree as ET
import os
import yaml
import json
from .utils import (
    is_directory,
    count_yaml_files,
    generate_report,
    get_jobtypes_andcount,
    generate_json,
    format_table_data
)

class Report():

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
        
        templatesToValidate = []
        ##Config_File_Info parameters 
        config_job_types_source = []
        config_job_types_source_count = 0
        ## Source_file_Info parameters
        source_files_count = 1
        source_file_info = []
        job_types_source= []
        job_types_source_count = 0

        ## Get the Job_types from config_file
        config_job_types_source, config_job_types_source_count = get_jobtypes_andcount(self.config_file)
        print("******config_JobType********")
        print(config_job_types_source)
        print(config_job_types_source_count)

        ## Get the Job_types from source xml
        if is_directory(self.source_path) is False:
            source_file_info.append(self.source_path.split("/")[-1])
            job_types_source, job_types_source_count = get_jobtypes_andcount(self.source_path)
            print("******SOURCEXML_JobType********")
            print(job_types_source)
            print(job_types_source_count)
        else:
            source_files_count = count_yaml_files(self.source_path)
            for filename in os.listdir(self.source_path):
                if filename.endswith('.yaml') or filename.endswith('.yml'):
                    source_file_info.append(filename)
            filename = os.path.basename(self.source_path)
            source_file_info.append(filename)
        print("******SOURCEXML********")
        print(source_file_info)
        print(source_files_count)

        ### Get templates INFO
        with open(self.config_file) as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise exc
        for idx, config in enumerate(self.config["config"]["mappings"]):
            # Set Command Uppercase
            self.config["config"]["mappings"][idx]["job_type"] = \
                self.config["config"]["mappings"][idx]["job_type"].upper()
            templatesToValidate.append(self.config["config"]["mappings"][idx]["template_name"])
        print("**************")
        print(templatesToValidate)
        print("**************")
        templates_count = count_yaml_files(self.templates_path)
        print("**************")
        print(templates_count)
        print("**************")

        ## Statistics Info parameters 
        converted_percentage = (config_job_types_source_count/job_types_source_count)*100
        non_converted_percentage = 0 if converted_percentage == 100 else (100-converted_percentage)
        
        ## Table Info
        statistics= [
            f"Percentage of Jobtypes converted: {converted_percentage}%", 
            f"Percentage of Jobtypes not converted: {non_converted_percentage}%"
            ]
        title = "DAGIFY REPORT"
        columns = ["TASK","INFO","COUNT"]
        rows = [
                ["Source_files", source_file_info, source_files_count],
                ["Job_Types", job_types_source, len(job_types_source)],
                ["Templates_validated", templatesToValidate, len(templatesToValidate)]
        ]
        
        formatted_table_data = format_table_data(title,columns,rows)

        generate_json(statistics,formatted_table_data,self.output_path)
        generate_report(statistics,title, columns, rows, self.output_path)

        ## Show which operators the job_type was converted to.
        ## Show the count with the job_name converted
        ## Details the job_names converted
        ## Remove the duplicates in the job_types list
