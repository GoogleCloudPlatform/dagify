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

import unittest
from converter import Config


class TestClass(unittest.TestCase):

    # Test That All Expected Converter Types have configuration
    def test_config_values_have_all_keys(self):

        # All Expected Values
        testKeys = {
            "UC4",
            "CONTROLM",
        }
        self.assertTrue(
            all(key in testKeys for key in Config().getConverters()))
        # whatever

    # Test That All Expected Converter Types have all the correct
    # configuration keys
    def test_config_converters_values_have_all_keys(self):

        # All Expected Values
        testKeys = {
            "id",
            "enabled",
            "name",
            "description",
        }
        for converter in Config().getConverters():
            self.assertTrue(all(key in testKeys for key in converter))


if __name__ == '__main__':
    unittest.main()