"""CNTRLM-TO-AIRFLOW entry point script."""
# controlm_parser/__main__.py

from controlm_parser import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()