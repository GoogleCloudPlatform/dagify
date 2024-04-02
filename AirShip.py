from AirShip.converter import Engine
import click

@click.command()
@click.option("--source-path", default="./source",
              help="Path to source files for conversion. Default: './source'")
@click.option("--output-path", default="./output",
              help="Path to output files after conversion. Default: './output'")
@click.option("--config-file", default="./config.yaml",
              help="Path to AirShip configuration file. Default: './config.yaml'")
@click.option("--templates", default="./AirShip/templates",
              help="Path to AirShip configuration file. Default: './AirShip/templates'")


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