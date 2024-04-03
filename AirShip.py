from AirShip.converter import Engine
import os
import click


@click.command()
@click.option("-s",
              "--source-path",
              default=lambda: os.environ.get("AS_SOURCE_PATH", "./source"),
              help="Path to source files for conversion",
              show_default="{}".format(
                  os.environ.get("AS_SOURCE_PATH",
                                 "./source")))
@click.option("-o",
              "--output-path",
              default=lambda: os.environ.get("AS_OUTPUT_PATH", "./output"),
              help="Path to output files after conversion.",
              show_default="{}".format(
                  os.environ.get("AS_OUTPUT_PATH",
                                 "./output")))
@click.option("-c",
              "--config-file",
              default=lambda: os.environ.get("AS_CONFIG_FILE",
                                             "./config.yaml"),
              help="Path to AirShip configuration file.",
              show_default="{}".format(
                  os.environ.get("AS_CONFIG_FILE",
                                 "./config.yaml")))
@click.option("-t",
              "--templates",
              default=lambda: os.environ.get("AS_TEMPLATES_PATH",
                                             "./AirShip/templates"),
              help="Path to AirShip configuration file.",
              show_default="{}".format(
                  os.environ.get("AS_TEMPLATES_PATH",
                                 "./AirShip/templates")))
def AirShip(source_path, output_path, config_file, templates):
    """Run AirShip."""
    print("Demo AirShip Engine")

    Engine(
        source_path=source_path,
        output_path=output_path,
        config_file=config_file,
        templates_path=templates,
    )


if __name__ == '__main__':
    AirShip()
