
## Cleaning 
clean: airship-clean
	@echo "Fully Cleaned!"
	
airship-clean: 
	@echo "Cleaning AirShip Package"
	rm -rf ./output
	rm -rf ./venv
	python3 -m venv ./venv
	. ./venv/bin/activate; pip install -r ./requirements.txt
	echo ${PWD}

# Containers
docker: docker-build docker-run
	@echo "Fully Containerized!"

docker-build: 
	@echo "Building the Docker Container"
	docker build -t localhost/airship:local . 

docker-run: 
	@echo "Running the Docker Container"
	docker run --env-file=.env.example localhost/airship:local

# Linting
lint: airship-lint
	@echo "Fully Linted!"

airship-lint:
	@echo "Linting the API Server Environment"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive --ignore=E402,E501 --exclude=./AirShip/venv ./AirShip
	flake8 --ignore=E402,E501 --exit-zero --exclude=./venv ./

# Building 
build: clean lint unit-tests int-tests docker-build
	@echo "Fully Cleaned and Built!"

# Local Run 
run: clean lint docker
	@echo "Fully Cleaned and Built!"

# run unit tests
unit-tests: 
	python3 -m unittest discover test

# run integration tests
int-tests:
	./AirShip/test/integration/run_integration-tests.sh

# run unit and integration tests
all-tests: unit-tests int-tests
	@echo "Completed execution of test suite"

licence: 
	docker run -i -t -v ${PWD}:/src ghcr.io/google/addlicense -c "Google LLC"  **/*.py