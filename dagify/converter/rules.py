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
    
    def rule_remove_back_ticks(self, vals):
        """Removes backticks from a string."""
        print(f"Info: Rule Remove Back Ticks applied to: {vals[0]}")
        if vals[0] and isinstance(vals[0], str):
            vals[0] = vals[0].replace('"', '')
            vals[0] = vals[0].replace("`", '')
            vals[0] = vals[0].replace("'", '')
        return vals[0]

    def rule_format_cmd_params(self, vals):
        """Formats command parameters, splitting them into separate arguments."""
        print(f"Info: Rule Format CMD Params applied to: {vals[0]}")
        if not vals[0] or not isinstance(vals[0], str):
            return vals[0]

        import re
        # Use regex to find patterns like 'date=value' and split them from the rest of the string
        # This regex will find assignments and the following variable
        pattern = r"([a-zA-Z0-9_]+=`.*?`)|(%%[A-Z0-9_]+%%)"
        parts = re.split(pattern, vals[0])
        
        # Filter out None and empty strings from the parts list
        parts = [p for p in parts if p and p.strip()]
        
        # The final command should be a list of strings
        formatted_parts = []
        temp_str = ""
        for p in parts:
            p = p.strip()
            if re.match(pattern, p):
                if temp_str:
                    formatted_parts.append(temp_str.strip())
                formatted_parts.append(p)
                temp_str = ""
            else:
                temp_str += " " + p
        
        if temp_str:
            formatted_parts.append(temp_str.strip())

        # For dagify, we return a string that will be split later
        return " ".join(formatted_parts)

    def rule_make_unique(self, vals):
        print(f"Info: Rule Make Unique: {vals[0]}")
        random.seed()
        rnd = random.randint(0, 1000000)
        uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(vals[0] + str(rnd))))[:5]
        vals[0] = self.rule_suffix([vals[0], uid])
        return vals[0]

    def rule_obfuscate(self, vals):
        print(f"Info: Rule Obfuscate: {vals[0]}")
        vals[0] = codecs.encode(vals[0], 'rot13')
        return vals[0]

    def rule_replace_hyphen_with_underscore(self, vals):
        print(f"Info: Rule Replace Hyphen with Underscore: {vals[0]}")
        vals[0] = vals[0].replace("-", "_")
        return vals[0]

    def rule_format_cmd_params(self, vals):
        print(f"Info: Rule Format CMD Params: {vals[0]}")
        import re
        
        # Pattern to find %%VARIABLES%%, including those inside strings
        pattern = r"%%(\w+)%%"
        
        # Replace all occurrences with the Jinja2 syntax
        def replace_var(match):
            var_name = match.group(1)
            return f"{{{{ params.{var_name} }}}}"

        # Use re.sub with a function for replacement
        formatted_cmd = re.sub(pattern, replace_var, vals[0])

        # Handle cases where the whole cmd is a variable that wasn't caught
        if vals[0].startswith("%%"):
            var_name = vals[0].replace("%%", "")
            return f"{{{{ params.{var_name} }}}}"

        # Split the command into parts, format them, and then join them back
        cmds = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', formatted_cmd)
        formatted_cmds = []
        for cmd in cmds:
            # remove quotes from start and end of string
            if cmd.startswith('"') and cmd.endswith('"'):
                cmd = cmd[1:-1]
            
            if cmd.startswith("{{"):
                formatted_cmds.append(cmd)
            else:
                formatted_cmds.append(f'"{cmd}"')
        
        return ",\n        ".join(formatted_cmds)

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
