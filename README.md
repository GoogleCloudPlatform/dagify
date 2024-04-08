<center>
    <span> <h1>AirShip</h1></span>
    <span> <h4><i>Migrate your enterprise scheduler workflows to Apache Airflow and Google Cloud Composer. </i></h4></span>
    <img src="./docs/assets/AirShip-Logo.png" alt="AirShip Logo" width="30%"/>
</center>
<br>

## AirShip Overview 
AirShip is a highly extensible, template driven, enterprise scheduler migration accelerator that helps organizations speed up their migration to Apache Airflow & Google Cloud Composer. While AirShip is not designed to be be a clear 1:1 migration tool it aims to heavily reduce the effort it takes for developers to convert their native enterprise scheduler formats into Native Python code in a Apache Airflow DAG format.  

The primary goal with AirShip is never to be 100% but rather reduce the number of human hours required to undertake the conversion and therefore speed up migrations! 
</br>

## Supported Features
This table outlines the schedulers that are currently supported by AirShip and which versions are currently considered. 

| Scheduler     | Feature         | Status | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | Convert Control-M  Folder -> Airflow DAG Mapping conversion | Under Development                |  |
| BMC Control-M | Convert Control-M  Job -> Airflow Task Mapping conversion | Under Development                |  |
| BMC Control-M | Convert Control-M Job Dependencies -> Airflow Dependencies conversion | Under Development                |  |
| BMC Control-M | Custom Calendars | Under Investigation                | Feasibility is not yet determined |
|               |                |                    |                             |

## Supported Schedulers
This table outlines the schedulers that are currently supported by AirShip and which versions are currently considered. 


| Scheduler     | Status         | Supported Versions | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | In Development | TBC                | Currently under development |
| UC4           | Roadmap        | TBC                | Only under consideration    |
|               |                |                    |                             |

# Running Locally
Here we outline how to run AirShip on your local machine.

## Start AirShip (From Source)

### With Defaults
```bash

make clean
python3 AirShip.py --source-path=[YOUR-SOURCE-XML-FILE]

```
Make clean; will create a new virtual environment using Python3 and install all required AirShip dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use the original mapping configuration yaml file in the root directory of the repo to conduct a conversion of your source file.

### With Custom Output Path and Custom Configuration File
```bash

make clean
python3 AirShip.py --source-path=[YOUR-SOURCE-XML-FILE] --output-path=[YOUR-OUTPUT-PATH] --config-file=[YOUR-CUSTOM-CONFIGURATION-YAML]

```
Make clean; will create a new virtual environment using Python3 and install all required AirShip dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use your custom original template mapping configuration yaml file to conduct a conversion of your source file. Additionally it will output the converted Python DAG files to the output directory provided in the above command. 

---


## Start AirLift (From Published Container)
> Comming Soon

---
# Command Line Help
You can get help from each command by running -h or --help next to the command

```bash
python3 AirShip.py --help
```
---

</br>

| Scheduler     | Feature         | Status | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | Convert Control-M  Folder -> Airflow DAG Mapping conversion | Under Development                |  |
| BMC Control-M | Convert Control-M  Job -> Airflow Task Mapping conversion | Under Development                |  |
| BMC Control-M | Convert Control-M Job Dependencies -> Airflow Dependencies conversion | Under Development                |  |
| BMC Control-M | Custom Calendars | Under Investigation                | Feasibility is not yet determined |
|               |                |                    |                             |

## Supported Schedulers
This table outlines the schedulers that are currently supported by AirShip and which versions are currently considered. 


| Scheduler     | Status         | Supported Versions | Notes                       |
|---------------|----------------|--------------------|-----------------------------|
| BMC Control-M | In Development | TBC                | Currently under development |
| UC4           | Roadmap        | TBC                | Only under consideration    |
|               |                |                    |                             |

# Running Locally
Here we outline how to run AirShip on your local machine.

## Start AirShip (From Source)

### With Defaults
```bash

make clean
python3 AirShip.py --source-path=[YOUR-SOURCE-XML-FILE]

```
Make clean; will create a new virtual environment using Python3 and install all required AirShip dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use the original mapping configuration yaml file in the root directory of the repo to conduct a conversion of your source file.

### With Custom Output Path and Custom Configuration File
```bash

make clean
python3 AirShip.py --source-path=[YOUR-SOURCE-XML-FILE] --output-path=[YOUR-OUTPUT-PATH] --config-file=[YOUR-CUSTOM-CONFIGURATION-YAML]

```
Make clean; will create a new virtual environment using Python3 and install all required AirShip dependencies using PIP into that virtual environment.

The above commands will use the built in default templates and also use your custom original template mapping configuration yaml file to conduct a conversion of your source file. Additionally it will output the converted Python DAG files to the output directory provided in the above command. 

---


## Run AirShip (From Local Container)
First you should update your .env.example file to use the environment variables you need. 
When you run the below commands you will mount your current working directory to the container for execution.
### With Defaults
```bash

docker build -t localhost/airship:source . 
docker run -it --env-file=.env.example -v $(pwd):/app localhost/airship:source

```
---


## Run AirShip (From Published Container)
> Coming Soon

---
# Command Line Help
You can get help from each command by running -h or --help next to the command

```bash
python3 AirShip.py --help
```
---

</br>
