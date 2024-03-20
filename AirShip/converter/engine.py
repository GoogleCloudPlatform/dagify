import os 
import yaml
from .utils import file_exists, clean_converter_type, create_directory, directory_extist, is_directory


class Engine(): 
    def __init__(self, templates_path="./templates", config_path="./config.yaml", source_file=None):
        self.templates_path = templates_path
        self.config_path = config_path
        self.source_file = source_file
        self.source_type = None
        
        # Run the Proccess 
        self.load_config()
        self.convert()
        
        

    def load_templates(self):  
        # This will load all templates from the provide path. 
        return
        
    def load_config(self):  
        
        # Validate Template Path Provided
        if self.config_path is None: 
            raise ValueError("AirShip: config file path not provided")
        if file_exists(self.config_path) is False:
            raise FileNotFoundError("AirShip: conifg path does not exist")
        
        with open(self.config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        # This will load the user provided config from the provide path. 
        # Store the config in a HASHMap or Similar and Provide a function for getting a 
        return
    
    def load_source(self): 
        # Read the Source File 
        # Parse into AirShip Universial Format
        # Output the AirShip Universial Format Back to the Class
        self.universal_format = None 
        return

    
    def convert(self):  
        """
         Read the Universal Format
         -->> Loop the Folders
           -->> Loop the Jobs
               --> GET the Config Mapping (Template) based on the Job Source Type;
                       [
                            
                       ]
               --> Read the Template Object from The Loaded Templates;
               --> Map the Field from Source -> Target Using the Template 
               --> Store the Python Task Def
               --> Store the YAML Task Def ()
               --> Store the Reporting Metrics and Findings for this Job.
           -->> Process Jobs and Build Dependencies
               --> Store Dependencies
           --> Construct DAG from all Stored Jobs
           --> Construct Report from all Stored Jobs Findings
           --> Construct YAML Output  from all Stored Jobs for "Dag Builder"
         --> Output all Files Created
        """
        
        for mapping in self.config["mappings"]: 
            print(mapping)
        
        return
        
    
    

    
    
    
        
     
     
     
     
     
        self.load_templates()

    def load_templates(self):
        # Validate Template Path Provided
        if self.templates_path is None: 
            raise ValueError("Parser: Templates path not provided")
        # Validate Template Directory Exists
        if directory_extist(self.templates_path) is False:
            raise FileNotFoundError("Parser: Templates path not provided")
        if is_directory(self.templates_path) is False:
            raise NotADirectoryError("Parser: Templates path is not a directory")
        
        # Load Templates
        for root, dirs, files in os.walk(self.templates_path):
            for file in files:
                if file.endswith(".yaml"):
                    print(os.path.join(root, file))
        return

    def convert(self):

        # Check Template Exsits
        if file_exists(file_path="./templates/001-control-m--ssh.yaml") is False:
                raise Exception("Parser: XML File does not exist at path provided")
        return

    

