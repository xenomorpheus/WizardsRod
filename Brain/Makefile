PYTHON ?= ../.venv/bin/python
SRC := brain/ tests/

.PHONY: all check autoformat format-check pycodestyle lint mypy test cover docs pipupdate

all: autoformat pycodestyle lint mypy cover docs

check: format-check pycodestyle lint mypy test

autoformat:
	@echo "===== autoformat ====="
	$(PYTHON) -m black $(SRC)

format-check:
	@echo "===== format check ====="
	$(PYTHON) -m black --check --diff $(SRC)

pycodestyle:
	@echo "===== pycodestyle ====="
	$(PYTHON) -m pycodestyle --max-line-length=120 $(SRC)

lint:
	@echo "===== lint ====="
	$(PYTHON) -m pylint --exit-zero $(SRC)

mypy:
	@echo "===== mypy ====="
	$(PYTHON) -m mypy $(SRC)

test:
	@echo "===== test ====="
	$(PYTHON) -m pytest

cover:
	@echo "===== coverage ====="
	$(PYTHON) -m pytest --cov=brain --cov-report=term --cov-report=html:doc/coverage

docs:
	@echo "===== docs ====="
	$(PYTHON) -m pdoc --force --html -o doc/ $(SRC)

pipupdate:
	pip --disable-pip-version-check list --outdated --format=json | python -c "import json, sys; print('\n'.join([x['name'] for x in json.load(sys.stdin)]))" | xargs -n1 pip install -U
