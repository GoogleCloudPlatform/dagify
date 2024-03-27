from converter import new_converter

def main():
    print("Demo Control-M Conversion")
    con = new_converter(converter_type="control-m")

    try:
        example_file = "examples/004-iron-giant.xml"

        con.analyze(example_file)
        con.parse(example_file)
    except Exception as e:
        print(str(e))
    return


if __name__ == '__main__':
    main()