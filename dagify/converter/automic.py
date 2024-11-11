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

from .utils import (
    load_source
)

from .engine import (
    set_baseline_imports,
    load_config,
    load_templates,
    validate,
    convert,
    cal_dag_dividers,
    calc_dag_dependencies,
    generate_airflow_dags
)

class Automic():
    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
        dag_divider="BranchType", # update if needed
    ):
        self.DAGs = []
        self.baseline_imports = []
        self.templates = {}
        self.templates_count = 0
        self.templates_path = templates_path
        self.config = {}
        self.config_file = config_file
        self.source_path = source_path
        source_xml_name = "-".join(self.source_path.split("/")[-1].split(".")[:-1])
        self.output_path = f"{output_path}/{source_xml_name}"
        self.dag_divider = "BranchType" if dag_divider == None else dag_divider # update if needed
        self.schema = "./dagify/converter/yaml_validator/schema.yaml"
        self.uf = load_source(self.source_path, "automic")

        # Run the Proccess
        set_baseline_imports(self)
        load_config(self)
        load_templates(self)
        validate(self)
        convert(self, "automic", "OType", "Object")
        cal_dag_dividers(self)
        calc_dag_dependencies(self.uf, "automic")
        generate_airflow_dags(self, "Object")
