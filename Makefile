install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:	
	black mylib/*.py

lint:
	ruff mylib/*.py
		
all: install lint test format
