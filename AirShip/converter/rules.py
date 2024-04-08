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

class Rule:
    def __init__(self):
        pass

    def run(self, args):
        method_name = "rule_{0}".format(args[0])
        if self.__can_execute(method_name):
            func = getattr(self, method_name)
            return func(args[1:])
        else:
            print(f"Rule not found: {args[0]}")
            return None
            
    def __can_execute(self, method_name):
        return method_name in dir(self)
    
    # Define Rules
    def rule_test(self, vals):
        print(f"Rule test: {vals[0]}")
        return vals[0]
