import os
import yamale
from dagify.converter.yaml_validator.custom_validator import validators


def validate(templates_path, schema_file):

    for root, dirs, files in os.walk(templates_path):
        for file in files:
            template_name = file.split(".")[0]
            print(f"{template_name} ready for validation")

            # Loads a Single Template into a Dictionary from .yaml file
            file_path = os.path.join(root, file)
            template = yamale.make_data(file_path)
            schema = yamale.make_schema(schema_file, validators=validators)

            if template is not None:

                try:
                    yamale.validate(schema, template)
                    print(f"Validation succeeded for {file}!")

                except yamale.YamaleError as e:
                    print(f"Validation failed for {file}!\n")
                    for result in e.results:
                        for error in result.errors:
                            print(error)
                    raise ValueError(f"Template {file_path} incompatible")


templates_path = "../dagify/dagify/templates"
schema_file = "../dagify/dagify/converter/yaml_validator/schema.yaml"
validate(templates_path, schema_file)
