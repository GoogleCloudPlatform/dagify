import os
import yamale
from dagify.converter.yaml_validator.custom_validator import validators


def validate_templates(directory, schema_file):
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

if __name__ == "__main__":
    directory="../../converter/templates",
    schema_file="../../converter/yaml_validator/schema.yaml",
    validate_templates(directory, schema_file)

