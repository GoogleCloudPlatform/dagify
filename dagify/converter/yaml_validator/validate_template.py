import os
import yamale
from custom_validator_yaml import validators

def validate_yaml_files_in_directory(directory, schema_file):
    # Load the schema
    schema = yamale.make_schema(schema_file, validators=validators)

    # List all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.yaml'):
            file_path = os.path.join(directory, filename)
            # Load the YAML file
            data = yamale.make_data(file_path)

            # Validate the data
            try:
                yamale.validate(schema, data)
                print(f"Validation succeeded for {filename}!")
            except yamale.YamaleError as e:
                print(f"Validation failed for {filename}!\n")
                for result in e.results:
                    for error in result.errors:
                        # Print only the custom error message
                        print(error)

def main(directory_path, schema_file):
    if not os.path.isdir(directory_path):
        print(f"The path {directory_path} is not a directory.")
        return
    if not os.path.isfile(schema_file):
        print(f"The file {schema_file} does not exist.")
        return
    validate_yaml_files_in_directory(directory_path, schema_file)

if __name__ == "__main__":
    # Example directory path and schema file
    directory_path = '/Users/harishsridhar/Projects/har_dagify/dagify/dagify/templates' # Change path here
    schema_file = './schema.yaml'
    main(directory_path, schema_file)