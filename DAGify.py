#!/usr/bin/env python3
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
import click
from dagify.converter import ControlM, Automic
from dagify.converter.report_generator import Report


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])




@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-s",
             "--source-path",
             default=lambda: os.environ.get("AS_SOURCE_PATH", "./source"),
             help="Path to source files for conversion",
             show_default="{}".format(
                 os.environ.get("AS_SOURCE_PATH",
                                "./source")))
@click.option("-o",
             "--output-path",
             default=lambda: os.environ.get("AS_OUTPUT_PATH", "./output"),
             help="Path to output files after conversion.",
             show_default="{}".format(
                 os.environ.get("AS_OUTPUT_PATH",
                                "./output")))
@click.option("-c",
             "--config-file",
             default=lambda: os.environ.get("AS_CONFIG_FILE",
                                            "./config.yaml"),
             help="Path to dagify configuration file.",
             show_default="{}".format(
                 os.environ.get("AS_CONFIG_FILE",
                                "./config.yaml")))
@click.option("-t",
             "--templates",
             default=lambda: os.environ.get("AS_TEMPLATES_PATH",
                                            "./dagify/templates"),
             help="Path to dagify configuration file.",
             show_default="{}".format(
                 os.environ.get("AS_TEMPLATES_PATH",
                                "./dagify/templates")))
@click.option("-d",
             "--dag-divider",
             help="Which field in Job Definition should be used to divide up DAGS.")

@click.option("-r",
             "--report",
             is_flag=True,
             default=False,
             help="Generate report in txt and json format which \
               gives an overview of job_types converted")

@click.option("--tool",
              type=click.Choice(['controlm', 'automic']),  # Restrict input to these choices
              default=lambda: os.environ.get("AS_TYPE", "controlm"),  # Default to 'ctrl-m'
              help="Type of conversion ('controlm' or 'automic')",
              show_default="{}".format(os.environ.get("AS_TYPE", "controlm")))

def dagify(source_path, output_path, config_file, templates, dag_divider, report, tool):
    """Run dagify."""
    print("Run DAGify Engine")

    if tool == "controlm":
        ControlM(
            source_path=source_path,
            output_path=output_path,
            config_file=config_file,
            templates_path=templates,
            dag_divider=dag_divider,
        )
    elif tool == "automic":
        Automic(
            source_path=source_path,
            output_path=output_path,
            config_file=config_file,
            templates_path=templates,
            dag_divider=dag_divider,
    )
        
    if report:
        Report(
            source_path=source_path,
            output_path=output_path,
            config_file=config_file,
            templates_path=templates,
            dag_divider=dag_divider,
        )

if __name__ == '__main__':
   dagify()