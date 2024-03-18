# AirShip
Migrate your enterprise scheudler workflows to Apache Airflow and Google Cloud Composer. 


</br></br>

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

## Running API Server Locally (Development Mode)
execute the following in the root directory of the project to start the application.

```bash

make api-clean
source app/venv/bin/activate
python3 app/wsgi.py

```
Then open the web application at http://localhost:8080

## Running Web Server Locally (Development Mode)
execute the following in the root directory of the project to start the application.

```bash

make web-clean
cd ./web
npm run dev

```
Then open the web application at http://localhost:8082


# Contribution 
We welcome contribuiton; At this time the contribution guidelines are still being created; Regardless of which, please always raise an issue on the github repository and we will get back to you as soon as possible. When raising issues please provide as much detail as possible and where ever possible please provide replication instructions and any other non PII or sensitive information that could help us understand the issue you are facing. 

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

