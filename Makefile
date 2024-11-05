# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Make will use bash instead of sh
SHELL := /usr/bin/env bash

## Cleaning 
clean: dagify-clean
	@echo "Fully Cleaned!"
	
dagify-clean: 
	@echo "Cleaning dagify Package"
	( \
		rm -rf ./output; \
		rm -rf ./venv; \
		python3 -m venv ./venv; \
		source ./venv/bin/activate; \
		pip install -r ./requirements.txt; \
	)
	echo ${PWD}

# Containers
docker: docker-build docker-run
	@echo "Fully Containerized!"

docker-build: 
	@echo "Building the Docker Container"
	docker build -t localhost/dagify:local . 

docker-run: 
	@echo "Running the Docker Container"
	docker run --env-file=.env.example localhost/dagify:local

# Linting
lint: dagify-lint
	@echo "Fully Linted!"

dagify-lint:
	@echo "Linting the API Server Environment"
	autopep8 -r -v -v -v --in-place --aggressive --aggressive --aggressive --ignore=E402,E501 --exclude=./dagify/venv ./dagify
	flake8 --ignore=E402,E501 --exit-zero --exclude=./venv ./

# Building 
build: clean lint unit-tests int-tests docker-build
	@echo "Fully Cleaned and Built!"

# Local Run 
run: clean lint docker
	@echo "Fully Cleaned and Built!"

# run unit tests
unit-tests: 
	python3 -m unittest discover --pattern=test*.py

# run integration tests
int-tests:
	./dagify/test/integration/run_integration-tests.sh

regenerate-int-tests:
	./dagify/test/integration/regenerate_int_tests.sh

# run unit and integration tests
all-tests: unit-tests int-tests
	@echo "Completed execution of test suite"

validate-templates:
	python3 validate_templates.py

licence: 
	docker run -i -t -v ${PWD}:/src ghcr.io/google/addlicense -c "Google LLC"  **/*.py
