<center>
    <span> <h1>DAGify</h1></span>
    <span> <h4><i>Migrate your enterprise scheduler workflows to Apache Airflow and Google Cloud Composer. </i></h4></span>
</center>
<br>

## DAGify Overview 
DAGify is a highly extensible, template driven, enterprise scheduler migration accelerator that helps organizations speed up their migration to Apache Airflow & Google Cloud Composer. While DAGify is not designed to be a clear 1:1 migration tool it aims to heavily reduce the effort it takes for developers to convert their native enterprise scheduler formats into native Python code in a Apache Airflow DAG format.  

The primary goal with DAGify is not to migrate 100% of existing scheduler workflows but rather reduce the number of human hours required to undertake the conversion and therefore speed up migrations! 
</br>

## Supported Features
This table outlines the schedulers that are currently supported by DAGify and which versions are currently considered. 


| Scheduler     | Feature         | Status | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | Convert Control-M  Folder -> Airflow DAG Mapping conversion | Under Development                |  |
| BMC Control-M | Convert Control-M  Job -> Airflow Task Mapping conversion | Under Development                |  |
| BMC Control-M | Convert Control-M Job Dependencies -> Airflow Dependencies conversion | Under Development                |  |
| BMC Control-M | Custom Calendars | Under Investigation                | Feasibility is not yet determined |
|               |                |                    |                             |

## Supported Schedulers
This table outlines the schedulers that are currently supported by DAGify and which versions are currently considered. 


| Scheduler     | Status         | Supported Versions | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | In Development | TBC                | Currently under development |
| UC4           | Roadmap        | TBC                | Only under consideration    |
|               |                |                    |                             |

# Running Locally
Here we outline how to run DAGify on your local machine.

## Start DAGify (From Source)

### With Defaults
```bash

make clean
python3 DAGify.py --source-path=[YOUR-SOURCE-XML-FILE]

```
Make clean; will create a new virtual environment using Python3 and install all required DAGify dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use the original mapping configuration yaml file in the root directory of the repo to conduct a conversion of your source file.

### With Custom Output Path and Custom Configuration File
```bash

make clean
python3 DAGify.py --source-path=[YOUR-SOURCE-XML-FILE] --output-path=[YOUR-OUTPUT-PATH] --config-file=[YOUR-CUSTOM-CONFIGURATION-YAML]

```
Make clean; will create a new virtual environment using Python3 and install all required DAGify dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use your custom original template mapping configuration yaml file to conduct a conversion of your source file. Additionally it will output the converted Python DAG files to the output directory provided in the above command. 

---

## Run DAGify (From Source Container)
First you should update your .env.example file to use the environment variables you need. 
When you run the below commands you will mount your current working directory to the container for execution.
### With Defaults
```bash

docker build -t localhost/dagify:source . 
docker run -it --env-file=.env.example -v $(pwd):/app localhost/dagify:source

```
---


## Run DAGify (From Published Container)

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
# Command Line Help
You can get help from each command by running -h or --help next to the command

```bash
python3 DAGify.py --help
```
---

</br>

