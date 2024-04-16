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


class UF():
    T = TypeVar('T', bound='UF')

    def __init__(self):
        self.tasks = []

    def from_controlm_xml(self: Type[T], node: xml.etree.ElementTree.Element):
        for key, value in node.attrib.items():
            # Set Original Attribute Version
            self.set_attribute_original(key, value)
            # Set Current Attribute Version
            self.set_attribute(key, value)
        self.set_raw_xml_element(node)

    # Handle Attributes
    def set_attribute_original(self, key, value):
        self.set_attribute(key + "_ORIGINAL", value)

    def set_attribute(self, key, value):
        setattr(self, key, value)

    def get_attribute_original(self, attribute: str) -> str:
        return self.get_attribute(attribute + "_ORIGINAL")

    def get_attribute(self, attribute: str) -> str:
        return getattr(self, attribute, None)

    # add task to the universal format
    def add_task(self, ufTask):
        self.tasks.append(ufTask)

    # get tasks from the universal format
    def get_tasks(self):
        return self.tasks
    
    # get total count of tasks from the universal format
    def get_task_count(self):
        return len(self.tasks)

    def set_raw_xml_element(self, node):
        self.raw_xml_element = node

    def get_raw_xml(self):
        return self.raw_xml_element
    
    #def calculate_dag_dependencies(self):
    #    deps = []
    #    # Calculate Job Dependencies for every job.
    #    for task in self.get_tasks():
    #        dep = ""
    #        out_conds = task.get_out_conditions()
    #        out_conds_positive = []

    #        for out_cond in out_conds:
    #            if out_cond.get_attribute("SIGN") == "+":
    #                out_conds_positive.append(out_cond)

    #        if len(out_conds_positive) > 0:
    #            items = ""

    #            for poutcon in out_conds_positive:
    #                for obj in self.get_tasks():
    #                    for in_conds in obj.get_in_conditions():
    #                        if in_conds.get_attribute("NAME") == poutcon.get_attribute("NAME"):
    #                            items += obj.get_attribute("JOBNAME") + ", "
    #            if items != "":
    #                dep = task.get_attribute("JOBNAME") + " >> [" + items + "]"
    #                dep = dep.replace(", ]", "]")

    #        if dep != "":
    #            deps.append(dep)

    #    if len(deps) > 0:
    #        self.dag_dependencies = deps
    #    else:
    #        self.dag_dependencies = []
            
    def calculate_dag_dependencies_v2(self):
        for task in self.get_tasks():
            dep = ""
            out_conds = task.get_out_conditions()
            out_conds_positive = []
            for out_cond in out_conds:
                if out_cond.get_attribute("SIGN") == "+":
                    out_conds_positive.append(out_cond)
            if len(out_conds_positive) > 0:
                items = ""
                
                for poutcon in out_conds_positive:
                    for obj in self.get_tasks():
                        for in_conds in obj.get_in_conditions():
                            if in_conds.get_attribute("NAME") == poutcon.get_attribute("NAME"):
                                    task.add_dependent_task(obj.get_dag_name(), obj.get_attribute("JOBNAME"))
        self.dag_dependencies = []

    def calculate_dag_python_imports(self, dag_divider_key="", dag_divider_value=""):
        python_imports = []
        dag_imps = {}
        for task in self.get_tasks():
            if task.get_attribute(dag_divider_key) == dag_divider_value or dag_divider_key == "":
                for task_import in task.get_airflow_task_python_imports():
                    if dag_imps.get(task_import['package'], None) is not None:
                        existing_imports = dag_imps.get(task_import['package'], None)
                        for new_imp in task_import['imports']:
                            if new_imp not in existing_imports:
                                dag_imps[task_import['package']].append(new_imp)

                    else:
                        dag_imps[task_import['package']] = task_import['imports']

                    # Sort the Import List
                    dag_imps[task_import['package']].sort()
        # Sort the Modules
        dag_imps = dict(sorted(dag_imps.items()))

        # Process to Pythonic Statements
        for package, imports_list in dag_imps.items():
            imports = ', '.join(imports_list)
            python_imports.append(f"from {package} import {imports}")

        # Set the Python Imports for the DAG
        return python_imports


class UFTask(UF):
    T = TypeVar('T', bound='UFTask')

    def __init__(self):
        self.variables = []
        self.in_conditions = []
        self.out_conditions = []
        self.shouts = []
        self.dep_tasks = []
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
        self.in_conditions.append(ufTaskInCondition)

    def get_in_conditions(self):
        return self.in_conditions

    def get_in_condition_count(self):
        return len(self.in_conditions)

    # Handle Out Conditions
    def add_out_condition(self, ufTaskOutCondition):
        self.out_conditions.append(ufTaskOutCondition)

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

    def set_airflow_task_output(self, output):
        self.airflow_task_output = output

    def get_airflow_task_output(self):
        return self.airflow_task_output

    def set_airflow_task_python_imports(self, imps):
        self.airflow_task_python_imports = imps

    def get_airflow_task_python_imports(self):
        return self.airflow_task_python_imports

    def get_output_raw_xml(self):
        xmlstr = xml.etree.ElementTree.tostring(self.raw_xml_element)
        return etree.tostring(
            etree.fromstring(xmlstr),
            pretty_print=True).decode()
    
    def set_dag_name(self, dag_name):
        self.dag_name = dag_name
        return
    
    def get_dag_name(self):
        return self.dag_name
    
    def get_dependent_tasks(self):
        return self.dep_tasks
    
    def add_dependent_task(self, dag_name, task_name): 
        self.dep_tasks.append({"dag_name": dag_name, "task_name": task_name})
        return


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
