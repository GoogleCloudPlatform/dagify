import xml.etree.ElementTree as ET
import os
import yaml
from .utils import (
    is_directory,
    count_yaml_files,
    generate_report,
    get_jobtypes_andcount
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
        source_files_count = 1
        source_file_info = []
        templatesToValidate = []
        job_types_source= []
        job_types_count = 0

        ## Get the Job_types
        if is_directory(self.source_path) is False:
            job_types_source, job_types_count = get_jobtypes_andcount(self.source_path)
            print("**************")
            print(job_types_source)
            print("**************")
            print(job_types_count)
            print("**************")
        else:
            source_files_count = count_yaml_files(self.source_path)
            for filename in os.listdir(self.source_path):
                if filename.endswith('.yaml') or filename.endswith('.yml'):
                    source_file_info.append(filename)
            filename = os.path.basename(self.source_path)
            source_file_info.append(filename)
        print("**************")
        print(source_file_info)
        print("**************")
        print("**************")
        print(source_files_count)
        print("**************")

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

        title = "DAGIFY REPORT"
        columns = ["TASK","INFO","COUNT"]
        rows = [
                ["Source_files", source_file_info, source_files_count],
                ["Job_Types", job_types_source, len(job_types_source)],
                ["Templates_validated", templatesToValidate, len(templatesToValidate)]
        ]
        generate_report(title, columns, rows, self.output_path)
