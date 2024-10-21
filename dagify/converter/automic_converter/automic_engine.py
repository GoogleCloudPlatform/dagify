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


class Automicengine():
    "Uc4/Automic conversion Engine"
    def __init__(
        self,
        source_path=None,
        output_path=None,
        templates_path="./templates",
        config_file="./config.yaml",
        dag_divider="PARENT_FOLDER",
    ):
        self.DAGs = []
        self.baseline_imports = []
        self.templates = {}
        self.templates_count = 0
        self.templates_path = templates_path
        self.config = {}
        self.config_file = config_file
        self.source_path = source_path
        source_xml_name = self.source_path.split("/")[-1].split(".")[0]
        self.output_path = f"{output_path}/{source_xml_name}"
        self.dag_divider = dag_divider
        self.schema = "./dagify/converter/yaml_validator/schema.yaml"
        