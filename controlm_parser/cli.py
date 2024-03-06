from typing import Optional
import typer
from controlm_parser import __app_name__, __version__
from controlm_parser.controlm_parser import ControlMParser

app = typer.Typer()

def _version_callback(value: bool) -> None:
  if value:
    typer.echo(f"{__app_name__} v{__version__}")
    raise typer.Exit()
  
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def parse(
  xml_path: str = typer.Option("xml/example.xml", "--xml_path"),
  folder_name: str = typer.Option(None, "--folder_name"),
  smart_folder_name: str = typer.Option(None, "--smart_folder_name"),
  output_path: str = typer.Option("output/dag.py", "--output_path"),
) -> None:
    """Run Control-M XML to Airflow DAG Conversion"""
    typer.echo(f"Running Control-M XML to Airflow DAG Conversion with parameters:")
    typer.echo(f"---")
    typer.echo(f"XML Path:          {xml_path}")
    typer.echo(f"Folder Name:       {folder_name}")
    typer.echo(f"Smart Folder Name: {smart_folder_name}")
    typer.echo(f"Output Path:       {output_path}")
    typer.echo(f"---")

    controlm_parser = ControlMParser(xml_path = xml_path,
                                folder_name = folder_name,
                                smart_folder_name = smart_folder_name,
                                output_path = output_path
                                )

    controlm_parser.parse()

    raise typer.Exit()

