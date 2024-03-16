# AirShip (Name TBD)

</br></br>

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
