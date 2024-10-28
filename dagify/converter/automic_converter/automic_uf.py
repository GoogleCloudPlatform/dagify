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

from typing import TypeVar, Type
import xml.etree.ElementTree
from lxml import etree

class AutomicUF():
    "Class for defining Automic UF object"
    T = TypeVar('T', bound='AutomicUF')

    def __init__(self):
        self.uf_parent_jobp = []

    def from_automic_xml(self: Type[T], node: xml.etree.ElementTree.Element):
        "Function to set attribute original and current names"
        for key, value in node.attrib.items():
            # Set Original Attribute Version
            self.set_attribute_original(key, value)
            # Set Current Attribute Version
            self.set_attribute(key, value)
        self.set_raw_xml_element(node)

    # Handle Attributes
    def set_attribute_original(self, key, value):
        "Function to set attribute original"
        self.set_attribute(key + "_ORIGINAL", value)

    def set_attribute(self, key, value):
        "Function to set attribute current"
        setattr(self, key, value)

    def get_attribute_original(self, attribute: str) -> str:
        "Function to get attribute original"
        return self.get_attribute(attribute + "_ORIGINAL")

    def get_attribute(self, attribute: str) -> str:
        "Function to get attribute current"
        return getattr(self, attribute, None)

    def set_raw_xml_element(self, node):
        self.raw_xml_element = node

    def get_output_raw_xml(self):
        xmlstr = xml.etree.ElementTree.tostring(self.raw_xml_element)
        return etree.tostring(
            etree.fromstring(xmlstr),
            pretty_print=True).decode()

    def get_raw_xml(self):
        return self.raw_xml_element

    # add parent_jobp to the universal format
    def add_parent_jobp(self, parentufjobp):
        "Function to add JOBP to uf object"
        self.uf_parent_jobp.append(parentufjobp)

    def get_parent_jobp(self):
        "Function to get JOBP from uf object"
        return self.uf_parent_jobp

    def get_parent_jobp_by_attr(self, attribute, value):
        "Function to get JOBP attributes from uf object"
        for task in self.uf_parent_jobp:
            if task.get_attribute(attribute) == value:
                return task
        return None

    def get_uf_parent_jobp_count(self):
        "Function to get JOBP count from uf object"
        return len(self.uf_parent_jobp)

class AutomicParentUFJobP(AutomicUF):
    "Class for defining and filling out Parent_Jobp_UF objects"
    T = TypeVar('T', bound='AutomicParentUFJobP')
    def __init__(self):
        self.uf_child_jobp = []
        #self.uf_jobpstruct = []
        #self.uf_task = []
        return

    # Handle Child JOBP values
    def add_child_jobp(self, childufjobp):
        "Function to add JOBP to uf object"
        self.uf_child_jobp.append(childufjobp)

    def get_child_jobp(self):                              
        "Function to get child JOBP from uf object"
        return self.uf_child_jobp

    def get_child_jobp_count(self):
        "Function to get count of childJOBP from uf object"
        return len(self.uf_child_jobp)

    # Handle JobpStruct
    # def add_jobp_struct(self,jobpstruct):
    #     "Function to add JOBPStruct to uf object"
    #     self.uf_jobpstruct.append(jobpstruct)

    # def get_jobp_struct(self):
    #     "Function to get JOBPStruct from uf object"
    #     return self.uf_jobpstruct

    # Add function for handling tasks
    # def add_tasks(self, UFJobPTask):
    #     self.uf_task.append(UFJobPTask)

    # def get_out_conditions(self):
    #     return self.uf_task

    # def get_out_condition_count(self):
    #     return len(self.uf_task)

class AutomicChildUFJobP(AutomicParentUFJobP):
    "Inherited special class for JOBP-tasks tags"
    T = TypeVar('T', bound='AutomicChildUFJobP')

    def __init__(self):
        #super().__init__()
        self.uf_jobpstruct = []
        return

    # Handle JobpStruct
    def add_jobp_struct(self,jobpstruct):
        "Function to add JOBPStruct to uf object"
        self.uf_jobpstruct.append(jobpstruct)

    def get_jobp_struct(self):
        "Function to get JOBPStruct from uf object"
        return self.uf_jobpstruct

    def get_get_jobp_struct_count(self):
        "Function to get count of childJOBP from uf object"
        return len(self.uf_jobpstruct)

class AutomicJobpStruct(AutomicParentUFJobP):
    "Inherited special class for JOBP-tasks tags"
    T = TypeVar('T', bound='AutomicJobpStruct')

    def __init__(self):
        self.uf_task = []
        return

    def add_tasks(self, UFJobPTask):
        self.uf_task.append(UFJobPTask)

    def get_out_conditions(self):
        return self.uf_task

    def get_out_condition_count(self):
        return len(self.uf_task)

class AutomicUFJobPTask(AutomicParentUFJobP):
    "Inherited special class for JOBP-tasks tags"
    T = TypeVar('T', bound='AutomicUFJobPTask')

    def __init__(self):
        return
