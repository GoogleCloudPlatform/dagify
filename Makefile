setup: 
	source .venv/bin/activate
	pip install -r requirements.txt

lint:
	flake8 ./controlm_parser