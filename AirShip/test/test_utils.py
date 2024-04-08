<<<<<<< HEAD
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
from converter import clean_converter_type


class TestClass(unittest.TestCase):
    def test_utils_func_clean_converter_type(self):
        self.assertEqual(clean_converter_type("1 2 3 4 5 6"), "123456")
        self.assertEqual(clean_converter_type("1_2-3!4*5() +6"), "123456")

    def test_utils_func_clean_converter_type_controlm_variants(self):
        self.assertEqual(clean_converter_type("control m"), "CONTROLM")
        self.assertEqual(clean_converter_type("control-m"), "CONTROLM")
        self.assertEqual(clean_converter_type("controlM"), "CONTROLM")
        self.assertEqual(clean_converter_type("ControlM"), "CONTROLM")
        self.assertEqual(clean_converter_type("Control-M"), "CONTROLM")
        self.assertEqual(clean_converter_type("Control_M"), "CONTROLM")
        self.assertEqual(clean_converter_type("Control M"), "CONTROLM")


if __name__ == '__main__':
    unittest.main()
=======
import unittest
from converter import clean_converter_type

class TestClass(unittest.TestCase):
  def test_utils_func_clean_converter_type(self):
      self.assertEqual(clean_converter_type("1 2 3 4 5 6"), "123456")
      self.assertEqual(clean_converter_type("1_2-3!4*5() +6"), "123456")
  def test_utils_func_clean_converter_type_controlm_variants(self):
      self.assertEqual(clean_converter_type("control m"), "CONTROLM")
      self.assertEqual(clean_converter_type("control-m"), "CONTROLM")
      self.assertEqual(clean_converter_type("controlM"), "CONTROLM")
      self.assertEqual(clean_converter_type("ControlM"), "CONTROLM")
      self.assertEqual(clean_converter_type("Control-M"), "CONTROLM")
      self.assertEqual(clean_converter_type("Control_M"), "CONTROLM")
      self.assertEqual(clean_converter_type("Control M"), "CONTROLM")
        

if __name__=='__main__':
  unittest.main()
>>>>>>> 45ce3a1 (Reworking the Converter products from the initail MVP into a Scalable, Testable and Imoprtable Python Package)
