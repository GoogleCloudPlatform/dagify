<center>
    <span> <h1>AirShip</h1></span>
    <span> <h4><i>Migrate your enterprise scheduler workflows to Apache Airflow and Google Cloud Composer. </i></h4></span>
</center>
<img style="text-align:center" src="./docs/assets/AirShip-Logo.png" alt="drawing" width="30%"/>
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
execute the following in the root directory of the project to start the application.

```bash

make run

```
Then open the web application at http://localhost:3000

---


## Start AirShip (From Published Container)
> Coming Soon

---

</br></br>

# Development
Here we outline how to run each of the components independently for development on your local machine.

# Contribution 
We welcome contribuiton; At this time the contribution guidelines are still being developed; Regardless of which, please always raise an issue on the github repository and we will get back to you as soon as possible. When raising issues please provide as much detail as possible and where ever possible please provide replication instructions and any other non PII or sensitive information that could help us understand the issue you are facing. 

## Contribution Areas

### Template Contribution (Primary)
AirShip utilizes templates to help map native scheduler formats to Apache Airflow Operator formats. Please consider whether the mapping you are requiring (example: Control-M Job --> Apache Airflow FTP or SSH Operator) is a pattern other users could benefit from. Template contribution is the best and easiest method of contributing to AirShip. 

### Rules & Custom Function Contribution
> Not Yet Available
AirShip is highly extensible and the ability to extend AirFlow by adding custom field conversion rules is an important part of our roadmap. Rules are applied to fields as they are converted from Source to AirFlow Operator. It is our desire that rules could be contributed and considered for all users. 

An example rule could be something as simple as ToUppercase() or ToLowercase() which takes the content of a field and converts it on route to its target mapping.  

## Branching Strategy 
Please note the branching strategy is as follows. Create a new branch based on the below naming conventions depending on the type of work you are contributing. Note that all branches will be checked for naming conventions before merging. 

When development is completed; Raise a PR from the development branch to the next available release branch; When the release is ready it will be merged by maintainers into the development branch and then merged into the master branch after testing and cooling off period. 

## Pull Requests
When development is completed you should raise a pull request from your development branch to next available release branch and request a Review. 

<center><span style="font-size:20px; font-weight:bold; text-align:center;">[Contributors Dev Branch] ---> [Release Branch release/vX.X.X] ---> [develop] ---> [main]</span></center></br></br>



## Branching Naming conventions  

Contributors should create branches that are prefixed based on the work they are covering along side their username for easy collection and identification:
Here are some example branch names depending on work type:

```
New Feature:
git checkout -b ft/<username>/<feature_description>
```

```
Bug Fix:
git checkout -b bug/<github_issue_number>/<fix_description>
```

```
GitHub Issue:
git checkout -b issue/<github_issue_number>/<username>/<description>
```

```
Refactor:
git checkout -b rf/<github_issue_number>/<username>/<description>
```


## Stargazers over time

[![Stargazers over time](https://starchart.cc/KonradSchieban/airship.svg)](https://starchart.cc/KonradSchieban/airship)