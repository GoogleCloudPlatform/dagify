from converter import Engine

def main():
    print("Demo AirShip Engine")
    engine = Engine(
        templates_path="./templates",
        config_path="./config.yaml",
        source_file="./examples/xxx.xml"
        #source_file="./examples/004-iron-giant.xml"
    )

if __name__ == '__main__':
    main()