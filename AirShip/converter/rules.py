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

import codecs
import pandas as pd
import random
import string
import uuid


class Rule:
    def __init__(self):
        pass

    def run(self, args):
        method_name = "rule_{0}".format(args[0])
        if self.__can_execute(method_name):
            func = getattr(self, method_name)
            return func(args[1:])
        else:
            print(f"Error: Rule not found: {args[0]}")
            return args[1]

    def __can_execute(self, method_name):
        return method_name in dir(self)

    # Define Rule - LowerCase
    def rule_lowercase(self, vals):
        print(f"Info: Rule Lowercase: {vals[0]}")
        vals[0] = vals[0].lower()
        return vals

    # Define Rule - Replace Characters
    def rule_replace(self, vals):
        print(f"Info: Rule Replace Characters: {vals[1]} -> {vals[2]} output = {vals[0]}")
        vals[0] = vals[0].replace(vals[1], vals[2])
        return vals

    # Define Rule - Python Variable Safe
    def rule_python_variable_safe(self, vals):
        print(f"Info: Rule Python Variable Safe: {vals[0]}")
        vals = self.rule_lowercase(vals)
        for char in ['-', ' ', '.', ':', ';', "$", "!", ",", "#"]:
            if char in vals[0]:
                vals = self.rule_replace([vals[0], char, "_"])
        return vals[0]

    def rule_prefix(self, vals):
        if len(vals) < 2:
            print("Error: Not Enough Variables passed to Prefix Rule")
            return
        print(f"Info: Rule Prefix: {vals[0]}")
        vals[0] = vals[1] + "_" + vals[0]
        return vals[0]

    def rule_suffix(self, vals):
        if len(vals) < 2:
            print("Error: Not Enough Variables passed to Suffix Rule")
            return

        print(f"Info: Rule Suffix: {vals[0]}")
        vals[0] = vals[0] + "_" + vals[1]
        return vals[0]

    def rule_escape_quotes(self, vals):
        print(f"Info: Rule Escape Quotes: {vals[0]}")
        for char in ["'", '"', "`"]:
            if char in vals[0]:
                vals = self.rule_replace([vals[0], char, f"\\{char}"])
        return vals[0]
    
    def rule_make_unique(self, vals):
        print(f"Info: Rule Make Unique: {vals[0]}")
        random.seed()
        rnd = random.randint(0, 1000000)
        uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(vals[0]+str(rnd))))[:5]
        vals[0] = self.rule_suffix([vals[0], uid])
        return vals[0]
    
    def rule_obfuscate(self, vals):
        print(f"Info: Rule Obfuscate: {vals[0]}")
        vals[0] = codecs.encode(vals[0], 'rot13')
        return vals[0]
    
    def rule_lookup_replace(self, vals):
        print(f"Info: Rule Lookup Replace: {vals[0]}")
        # vals[0] is Lookup Value
        # vals[1] is Lookup File Path
        # vals[2] is Lookup Return Column
        
        if len(vals) < 3:
            print("Error: Not Enough Variables passed to Lookup Replace Rule")
            return vals[0]
        
        df = pd.read_csv(vals[1], header=0)
        print(df)
        
        return vals[0]