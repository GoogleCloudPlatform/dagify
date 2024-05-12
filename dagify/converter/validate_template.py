import yaml
from collections import defaultdict
import re, os
import requests

class templateParser():

    def __init__(self):
        self.keys_by_indentation = defaultdict(list)
        self.flattened_dictionary = []

        self.required_keys = defaultdict(set)
        self.required_keys[0] = set(['metadata','source','target','mappings','structure'])
        self.required_keys[1] = set(
            [
                'metadata.id','metadata.name','metadata.version','metadata.author','metadata.description-short','metadata.description',
                'source.platform','source.operator',
                'target.platform', 'target.operator',
            ])
        self.required_keys[2] = set(['metadata.author.name','metadata.author.email',
        'source.platform.id','source.platform.name','source.operator.id',
        'target.platform.id','target.platform.name',
        'target.operator.id','target.operator.name','target.operator.docs','target.operator.imports',

        ])

    
    def file_exists(self,file_path):
        """Checks if a file exists.

        Args:
            file_path (str): The path to the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        file_path = os.path.abspath(file_path)
        return os.path.isfile(file_path)
    
    def read_yaml_to_dict(self,yaml_file):
        """Loads a YAML file into a dictionary.

        Args:
            yaml_file (str): The path to the YAML file.

        Returns:
            dict: The dictionary representation of the YAML file.
        """
        if yaml_file is None or not self.file_exists(yaml_file):
            raise FileNotFoundError(
                "AirShip: template file provided is None or does not exist")
            return

        with open(yaml_file, 'r') as file:
            return yaml.safe_load(file)

    
    def flatten_dict(self,dictionary, parent_key, indentation):
        """A recursive function that flattens a nested dictionary into a single level using dot notation.

        Args:
            dictionary (dict): The dictionary representation of the YAML file
            parent_key : A built up prefix for each key in the dictionary
            indentation : A variable to indicate the level of nesting 

        Returns:
            A flattened dictionary 
        
        Class Variable:
            keys_by_indentation - Another dictionary that only stores the key, and at what layer of indentation it was in the file
        """
        
        
        for current_key, current_val in dictionary.items():
            
            # If previous level of indentation exists
            if indentation : 
                nested_key = parent_key + "." + current_key
                
            else:
                nested_key = current_key
            

            self.keys_by_indentation[indentation].append(nested_key)
            # If the current_value itself is a dictionary, it must be flattened again - hence the recursive call
            if isinstance(current_val, dict): 

                # nested_key becomes new parent
                # current_val becomes new dictionary
                self.flattened_dictionary.extend(self.flatten_dict(current_val, nested_key,indentation+1).items())

            elif isinstance(current_val,list):
                
                for component in current_val:
                    if isinstance(component,dict):
                        self.flattened_dictionary.extend(self.flatten_dict(component, nested_key,indentation+1).items())

                ## To work on - since keys are unique in a dictionary, tags overwrites each time in the list ##
                # tags : control-m, ssh etc
                """
                if isinstance(current_val[0],str):
                    for string_element in current_val:
                        print("string",string_element)
                        self.flattened_dictionary.append((nested_key, string_element))   
                        print(self.flattened_dictionary)     
                """

            else:

                # The generated (k,v) tuple is appended to the list
                self.flattened_dictionary.append((nested_key, current_val))

        # The list is converted into a dictionary
        return defaultdict(str, dict(self.flattened_dictionary)) 


    def validate_template(self,keys_by_indentation, flattened_dictionary):
        """A function that validates the key value pairs in the flattened_dictionary
        
        Args:
            required_keys (dict): A class variable that has the expected keys in the template
            parent_key : A built up prefix for each key in the dictionary

        Class Variables:
            keys_by_indentation (dict) : Stored all the keys of the template based on level of indentation
            required_keys (dict) : Stored all the expected/ compulsory keys of the template based on level of indentation

        """

        indentations = len(keys_by_indentation)

        for indentation in range(indentations): 

            keys_in_template = set(keys_by_indentation[indentation])
            required_keys = self.required_keys[indentation]

            for key in required_keys:
                if key not in keys_in_template:
                    print("missing key", key, "\n")
            
            ## Validate that the values in yaml are correct ##
            for key in keys_by_indentation[indentation]:
                # Things like "target" , "target.platform" should be skipped as those are parent keys without and immediate value
                if key in flattened_dictionary: 
                    value = flattened_dictionary[key]

                    # Value is missing entirely #
                    if value == "" or value ==None:
                        print("for key",key, "corresponding value should not be null","\n")
                        
                    # Generic Tests from the last keyword #
                    last_keyword = key.split(".")[-1]
              
                    if last_keyword == "email":                    
                        pattern = re.compile("^[a-zA-Z0-9][\\s]+")
                        if pattern.match(value) == None:
                            print(key, "does not have a valid email","\n")

                    elif last_keyword == "docs":
                        try:
                            response = requests.get(value)
                            return response.status_code == 200
                        except requests.exceptions.RequestException as e:
                            print(f"Error checking URL: {e}")
                            # return False

                    # Specific tests
                    if key == "metadata.description-short":
                        if len(value) > 256 :
                            return "Description size too big" 


parser = templateParser()
yaml_file = "./dagify/dagify/templates/control-m-command-to-airflow-gke-start-job.yaml"
template_dictionary = parser.read_yaml_to_dict(yaml_file)
flattened_dictionary = parser.flatten_dict(template_dictionary,"",0)
keys_by_indentation = parser.keys_by_indentation
parser.validate_template(keys_by_indentation,flattened_dictionary)
print("\n")








