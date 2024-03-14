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
	docker run localhost/airlift:v0.0.1 -p 3000:8080

# Linting
lint: api-lint web-lint
	@echo "Fully Linted!"

web-lint:
	@echo "Linting the Web Server Environment"

api-lint:
	@echo "Linting the API Server Environment"
	flake8 --exit-zero --exclude=./app/venv ./app

# Building 
build: clean lint docker-build
	@echo "Fully Cleaned and Built!"

# Local Run 
run: clean lint docker
	@echo "Fully Cleaned and Built!"
