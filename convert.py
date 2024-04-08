from controlm_parser.controlm_parser import ControlMParser

if __name__ == "__main__":

    xml_path = "xml/example.xml"
    folder_name = None
    smart_folder_name = "Box2"
    output_path = "output/dag.py"
    controlm_parser = ControlMParser(xml_path=xml_path,
                                     folder_name=folder_name,
                                     smart_folder_name=smart_folder_name,
                                     output_path=output_path
                                     )

    controlm_parser.parse()
