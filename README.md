<center>
    <span> <h1>DAGify</h1></span>
    <span> <h4><i>Migrate your enterprise scheduler workflows to Apache Airflow and Google Cloud Composer. </i></h4></span>
</center>
<br>

## Table of Contents
**[DAGify Overview](#dagify-overview)**<br>
**[Running Locally](#running-locally)**<br>
**[Templates](#templates)**<br>
**[Supported Features](#supported-features)**<br>
**[Supported Schedulers](#supported-schedulers)**<br>

## DAGify Overview 
DAGify is a highly extensible, template driven, enterprise scheduler migration accelerator that helps organizations speed up their migration from Control-M to Apache Airflow & Google Cloud Composer. It aims to heavily reduce the effort it takes for developers to convert their native enterprise scheduler formats into native Python code in a Apache Airflow DAG format.  

DAGify's ambition is not to migrate 100% of existing scheduler workflows but rather reduce the number of human hours required to undertake the conversion and therefore speed up migrations!

---

## Disclaimer
This is not an officially supported Google product. This tool is intended to help users to migrate their Control-M jobs to Apache Airflow.

---
## Running Locally
Here we outline how to run DAGify on your local machine.

### Start DAGify (From Source)

#### With Defaults
```bash

make clean
python3 DAGify.py --source-path=[YOUR-SOURCE-XML-FILE]

```
Make clean; will create a new virtual environment using Python3 and install all required DAGify dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use the original mapping configuration yaml file in the root directory of the repo to conduct a conversion of your source file.

#### With Custom Output Path and Custom Configuration File
```bash

make clean
python3 DAGify.py --source-path=[YOUR-SOURCE-XML-FILE] --output-path=[YOUR-OUTPUT-PATH] --config-file=[YOUR-CUSTOM-CONFIGURATION-YAML]

```
`make clean` will create a new virtual environment using Python3 and install all required DAGify dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use your custom original template mapping configuration yaml file to conduct a conversion of your source file. Additionally it will output the converted Python DAG files to the output directory provided in the above command. 

#### Commandline help

Do get an overview over all commandline parameters , their usage and purpose, simply run 
```bash
python3 DAGify.py -h
```
or
```bash
python3 DAGify.py --help
```

---

### Run DAGify (From Source Container)
First you should update your .env.example file to use the environment variables you need. 
When you run the below commands you will mount your current working directory to the container for execution.
#### With Defaults
```bash

docker build -t localhost/dagify:source . 
docker run -it --env-file=.env.example -v $(pwd):/app localhost/dagify:source

```
---


### Run DAGify (From Published Container)

First you should create a ```data``` directory on your local machine. Place your xml file or files in that data directory.

Then run the remote container while mounting the local ```data``` directory to the container (```-v ${PWD}/data:/app/data```) in addition you should pass the direct path to the XML file within the data directory to the environment variable ```AS_SOURCE_PATH``` for example: (```-e AS_SOURCE_PATH=./data/test.xml```). You should also set the output directory environment variable ```AS_SOURCE_PATH``` to a folder within the data directory (```-e AS_OUTPUT_PATH=./data/output```). 

You can run the following to use the tool;

```bash
mkdir data
# Add your Source XML file to the /data directory
mkdir data/output

# run the container
docker run -it \
    -e AS_SOURCE_PATH=./data/test.xml \
    -e AS_OUTPUT_PATH=./data/output \
    -v ${PWD}/data:/app/data \
    europe-docker.pkg.dev/dagify/dagify/dagify:latest  

# view the output Airflow DAG's in /data/output

```

---
## DAG Dividers

If you have a large Control-M XML file you may consider splitting the Airflow tasks into multiple DAGs. DAGify has a commandline parameter `-d` or `--dag-divider` which specifies by which XML attribute jobs should be divided by. For example, you may have your Control-M jobs in a single folder but in distinct applications and sub-applications. If you want to create all tasks in a single DAG run:
```bash
./DAGify -d FOLDER
```

If you want to generate several DAGs that are separated by Control-M application, run:
```bash
./DAGify -d APPLICATION
```
or alternatively to seprate by sub-application:
```bash
./DAGify -d SUB_APPLICATION
```


---
## Templates
DAGify employs a flexible template system that empowers you to define the mapping between Control-M jobs and Airflow operators. These user-defined YAML templates specify how Control-M attributes translate into Airflow operator parameters. For instance, the [control-m-command-to-airflow-ssh](./dagify/templates/control-m-command-to-airflow-ssh.yaml) template maps Control-M's "Command" task type to Airflow's SSHOperator, outlining how attributes like JOBNAME and CMDLINE are incorporated into the generated DAG.
The template's structure field utilizes Jinja2 templating to dynamically construct the Airflow operator code, seamlessly integrating Control-M job attributes.

Example: Consider the following Control-M job in an XML file:
```xml
<JOB 
  APPLICATION="my_application" 
  SUB_APPLICATION="my_sub_application" 
  JOBNAME="job_1" 
  DESCRIPTION="job_1_reports"  
  TASKTYPE="Command" 
  CMDLINE="./hello_world.sh" 
  PARENT_FOLDER="my_folder">
  <OUTCOND NAME="job_1_completed" ODATE="ODAT" SIGN="+" />
</JOB>
```

With the [control-m-command-to-airflow-ssh](./dagify/templates/control-m-command-to-airflow-ssh.yaml) yaml templates, this job will be converted to:
```python
job_1 = SSHOperator(
    task_id="x_job_1",
    command="./hello_world.sh",
    dag=dag,
)
```

The repository includes several pre-defined templates for common Control-M task types. The [config.yaml](./config.yaml) file allows you to customize which templates are applied during the conversion process.

A template has the following structure:

```yaml
--- 
metadata:
#(...omitted)
source:
  platform: 
    id: "CONTROLM"
    name: "Control-M"
  operator: 
    id: "Command" # the job type in Control-M that should be converted
target:
  platform: 
      id: "APACHEAIRFLOW"
      name: "Apache Airflow"
  operator: 
      id: "BashOperator" # the Airflow operator that the job should be converted to
      name: "Bash Operator"
      docs: "https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html"
      imports: 
        - package: "airflow.operators.bash" # the Python package that contains the operator
          imports:
              - "BashOperator" # the Python module inside the Python package
mappings:
  - source: JOBNAME                # Attribute name in Control-M XML file
    target: task_id                # Target variable that will be used in the "structure" section below
    rules:                         # Any rules that should be applied to this mapping
      - rule: python_variable_safe # Rule function that will be applied to the target
  - source: CMDLINE
    target: command
    rules:
      - rule: escape_quotes
structure: | # The Airflow operator that will be generated in the converted Python file. Target variables from the "mappings" section will replace the tokens in curly braces.
  {task_id} = BashOperator(
    task_id="{task_id}",
    bash_command="{command}",
    dag=dag,
  )
```

---
## Rules Engine
Rules can be applied to to the target variables that are defined in the conversion template. An example use cases for a rule is the need to replace characters in Control-M job names (e.g. `$`) to underscores because they might be illegal characters in Python variables.

Rules are Python functions that are defined in the [rules.py](./dagify/converter/rules.py) file. Apply the rules in the "mappings" section of the conversion template.

---
## Supported Features
This table outlines the schedulers that are currently supported by DAGify and which versions are currently considered. 


| Scheduler     | Feature         | Status | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | Convert Control-M  Folder -> Airflow DAG Mapping conversion | Ready                |  |
| BMC Control-M | Convert Control-M  Job -> Airflow Task Mapping conversion | Ready                |  |
| BMC Control-M | Convert Control-M Job Dependencies -> Airflow Dependencies conversion | Ready                |  |
| BMC Control-M | Custom Calendars | Under Investigation                | Feasibility is not yet determined |
|               |                |                    |                             |

## Supported Schedulers
This table outlines the schedulers that are currently supported by DAGify and which versions are currently considered. 


| Scheduler     | Status         | Supported Versions | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | Beta Release   | TBC                | Beta Release ready for testing |
| UC4           | Roadmap        | TBC                | Only under consideration    |
|               |                |                    |                             |

## Generate a Conversion Status Report
To generate a detailed report on the conversion process, include the **-r** parameter in your command. The report will be saved in the same output folder (customizable using the -o parameter). Key information included in the report:

Conversion Summary: Overall conversion statistics, including the count and percentage of converted TASKTYPEs.
Conversion Details: A comprehensive table outlining specific TASKTYPE conversions, jobs requiring manual approval, and utilized templates.
Schedule Adjustments: A separate table detailing any changes made to job schedules during the conversion.

---

</br>

