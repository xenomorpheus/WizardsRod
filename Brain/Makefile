all: test lint

test:
	#PYTHONPATH=. py.test tests
	python3 -m pytest tests/*.py

lint:
	pylint --py3k *.py tests/*.py

