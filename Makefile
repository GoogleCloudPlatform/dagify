
## Cleaning 
clean: airship-clean
	@echo "Fully Cleaned!"
	
airship-clean: 
	@echo "Cleaning AirShip Package"
	rm -rf ./venv
	python3 -m venv ./venv
	. ./venv/bin/activate; pip install -r ./requirements.txt

# Containers
docker: docker-build docker-run
	@echo "Fully Containerized!"

docker-build: 
	@echo "Building the Docker Container"
	docker build -t localhost/airship:v0.0.1 . 

docker-run: 
	@echo "Running the Docker Container"
	docker run --env-file=docker.env localhost/airship:v0.0.1

# Linting
lint: airship-lint
	@echo "Fully Linted!"

airship-lint:
	@echo "Linting the API Server Environment"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive --ignore=E402 --exclude=./AirShip/venv ./AirShip
	flake8 --exit-zero --exclude=./AirShip/venv ./AirShip

# Building 
build: clean lint docker-build
	@echo "Fully Cleaned and Built!"

# Local Run 
run: clean lint docker
	@echo "Fully Cleaned and Built!"

# run tests
tests: 
	python3 -m unittest discover test