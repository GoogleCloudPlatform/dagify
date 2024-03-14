# AirLift (Name TBD)


# Development
Here we outline how to run each of the components independently for development on your local machine.

## Running API Server Locally (Development Mode)
```bash

make api-clean
source app/venv/bin/activate
python3 wsgi.py

```

## Running Web Server Locally (Development Mode)
```bash

make web-clean
cd ./web
npm run dev

```
