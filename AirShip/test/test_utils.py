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
