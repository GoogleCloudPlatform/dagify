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


def base_apply(string):
    string = string.lower()
    string = string.replace("-", "_")
    string = string.replace(":", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("#", "_")
    string = string.replace(" ", "_")
    return string


class UF():
    T = TypeVar('T', bound='UF')

    def __init__(self):
        self.folders = []

    def from_controlm_xml(self: Type[T], node: xml.etree.ElementTree.Element):
        for key, value in node.attrib.items():
            setattr(self, base_apply(key), value)
        self.set_raw_xml_element(node)

    # Handle Attributes
    def get_attribute(self, attribute: str) -> str:
        return getattr(self, base_apply(attribute), None)

    # add folder to the universal format
    def add_folder(self, ufFolder):
        self.folders.append(ufFolder)

    # get folders from the universal format
    def get_folders(self):
        return self.folders

    # get total count of folders from the universal format
    def get_folder_count(self):
        return len(self.folders)

    def set_raw_xml_element(self, node):
        self.raw_xml_element = node

    def get_raw_xml(self):
        return self.raw_xml_element


class UFFolder(UF):
    T = TypeVar('T', bound='UFFolder')

    def __init__(self):
        self.tasks = []

    def add_task(self, ufTask):
        self.tasks.append(ufTask)

    def get_tasks(self):
        return self.tasks

    def get_task_count(self):
        return len(self.tasks)


class UFTask(UF):
    T = TypeVar('T', bound='UFTask')

    def __init__(self):
        self.variables = []
        self.in_conditions = []
        self.out_conditions = []
        self.shouts = []
        return

    # Handle Variables
    def add_variable(self, ufTaskVariable):
        self.variables.append(ufTaskVariable)

    def get_variables(self):
        return self.variables

    def get_variable_count(self):
        return len(self.variables)

    # Handle In Conditions
    def add_in_condition(self, ufTaskInCondition):
        self.variables.append(ufTaskInCondition)

    def get_in_conditions(self):
        return self.in_conditions

    def get_in_condition_count(self):
        return len(self.in_conditions)

    # Handle Out Conditions
    def add_out_condition(self, ufTaskOutCondition):
        self.variables.append(ufTaskOutCondition)

    def get_out_conditions(self):
        return self.out_conditions

    def get_out_condition_count(self):
        return len(self.out_conditions)

    # Handle SHOUTS Conditions
    def add_shout(self, ufTaskShout):
        self.variables.append(ufTaskShout)

    def get_shouts(self):
        return self.shouts

    def get_shout_count(self):
        return len(self.shouts)

    def set_output_airflow_task(self, output):
        self.output_airflowtask = output

    def get_output_airflow_task(self):
        return self.output_airflowtask

    def get_output_raw_xml(self):
        xmlstr = xml.etree.ElementTree.tostring(self.raw_xml_element)
        return etree.tostring(
            etree.fromstring(xmlstr),
            pretty_print=True).decode()


class UFTaskVariable(UFTask):
    T = TypeVar('T', bound='UFTaskVariable')

    def __init__(self):
        return


class UFTaskInCondition(UFTask):
    T = TypeVar('T', bound='UFTaskInCondition')

    def __init__(self):
        return


class UFTaskOutCondition(UFTask):
    T = TypeVar('T', bound='UFTaskOutCondition')

    def __init__(self):
        return


class UFTaskShout(UFTask):
    T = TypeVar('T', bound='UFTaskShout')

    def __init__(self):
        return
