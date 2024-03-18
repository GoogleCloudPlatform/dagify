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
    self.assertTrue(all(key in testKeys for key in Config().getConverters()))
    # whatever
  
  # Test That All Expected Converter Types have all the correct configuration keys
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

if __name__=='__main__':
  unittest.main()