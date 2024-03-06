# CNTRLM-TO-AIRFLOW

This repository contains a tool written in Python3 that converts Control-M XML files to Apache Airflow DAGs.

## Disclaimer

This is not an officially supported Google product. This tool is intended to help users converting Control-M XML files to Airflow DAG files.

## Usage

### UNIX Commandline

To get started with *CNTRLM-TO-AIRFLOW* follow the steps below:

1. Clone this repository and navigate to the root of this folder.
```
$ git clone https://github.com/KonradSchieban/cntrlm-to-airflow.git
$ cd cntrl-to-airflow
```

2. Create a Python Virtual Environment:
```
$ python3 -m venv ./venv
$ source venv/bin/activate
```

3. Install pip requirements
```
pip install -r requirements.txt
```

4. Run XML conversion by calling the controlm_parser library module
```
python3 -m controlm_parser parse --smart_folder_name Box1 --xml_path xml/example.xml --output_path output/dag.py
```

### Docker

...TBD
