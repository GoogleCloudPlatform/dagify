## Cleaning 
clean: api-clean web-clean
	@echo "Fully Cleaned!"

web-clean:
	@echo "Cleaning Web Server Environment"
	rm -rf ./web/node_modules
	rm -rf ./web/dist
	npm --prefix ./web install
	
api-clean: 
	@echo "Cleaning API Server Environment"
	rm -rf ./app/venv
	python3 -m venv ./app/venv
	. ./app/venv/bin/activate; pip install -r ./app/requirements.txt

# Containers
docker: docker-build docker-run
	@echo "Fully Containerized!"

docker-build: 
	@echo "Building the Docker Container"
	docker build -t localhost/airlift:v0.0.1 . 

docker-run: 
	@echo "Running the Docker Container"
	docker run -p 3000:8080 localhost/airlift:v0.0.1

# Linting
lint: con-lint api-lint web-lint
	@echo "Fully Linted!"

web-lint:
	@echo "Linting the Web Server Environment"

api-lint:
	@echo "Linting the API Server Environment"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive --exclude=./app/venv ./app
	flake8 --exit-zero --exclude=./app/venv ./app

con-lint:
	@echo "Linting the Converter Modules"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive ./converters
	flake8 --exit-zero ./converters

# Building 
build: clean lint docker-build
	@echo "Fully Cleaned and Built!"

# Local Run 
run: clean lint docker
	@echo "Fully Cleaned and Built!"
