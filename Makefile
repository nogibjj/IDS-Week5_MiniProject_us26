install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black mylib/*.py 
	black *.py

lint:
	ruff mylib/*.py
		
all: install lint test format
