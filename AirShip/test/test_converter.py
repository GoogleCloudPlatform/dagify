import unittest
from converter import new_converter, ControlMConverter


class TestClass(unittest.TestCase):
    def test_new_converter_controlm_valid(self):
        pass
    # Test Control-M with Mixed Cases
        # self.assertEqual(new_converter(converter_type="Control-M"), type(ControlMConverter))
    # Test Control-M with All Lowercase
        # con = new_converter(converter_type="control-m")
    # Test Control-M with All Uppercase
        # con = new_converter(converter_type="CONTROL-M")
    # Test Control-M with Mixed Cases No Hyphen
        # con = new_converter(converter_type="cOnTroLm")


if __name__ == '__main__':
    unittest.main()
