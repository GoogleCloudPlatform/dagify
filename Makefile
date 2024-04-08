
## Cleaning 
clean: airship-clean
	@echo "Fully Cleaned!"
	
airship-clean: 
	@echo "Cleaning AirShip Package"
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
	docker run --env-file=.env.local localhost/airship:local

# Linting
lint: airship-lint
	@echo "Fully Linted!"

airship-lint:
	@echo "Linting the API Server Environment"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive --ignore=E402,E501 --exclude=./AirShip/venv ./AirShip
	flake8 --ignore=E402,E501 --exit-zero --exclude=./venv ./

con-lint:
	@echo "Linting the Converter Modules"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive ./converters
	flake8 --exit-zero ./converters

# Building 
build: clean lint tests docker-build
	@echo "Fully Cleaned and Built!"

# Local Run 
run: clean lint docker
	@echo "Fully Cleaned and Built!"

# run tests
tests: 
	python3 -m unittest discover test

licence: 
	docker run -i -t -v ${PWD}:/src ghcr.io/google/addlicense -c "Google LLC"  **/*.py
