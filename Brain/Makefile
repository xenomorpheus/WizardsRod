all: autoformat pycodestyle lint mypy test cover docs


autoformat:
	@echo "===== autoformat ====="
	black --line-length=120  brain/ tests/

pycodestyle:
	@echo "===== pycodestyle ====="
	pycodestyle --max-line-length=120 brain/ tests/

lint:
	@echo "===== Lint ====="
	pylint --exit-zero brain/ tests/ || true

mypy:
	@echo "===== MyPy ====="
	mypy brain/ tests/ || true

test:
	pytest

cover:
	coverage3 erase
	PYTHONPATH=. coverage3 run --branch --append --source=brain tests/test_spelllistprepared.py
	PYTHONPATH=. coverage3 run --branch --append --source=brain tests/test_spell.py
	PYTHONPATH=. coverage3 run --branch --append --source=brain tests/test_spelltriggergesture.py
	PYTHONPATH=. coverage3 run --branch --append --source=brain tests/test_spelltrigger.py
	PYTHONPATH=. coverage3 run --branch --append --source=brain tests/test_staffevent.py
	PYTHONPATH=. coverage3 run --branch --append --source=brain tests/test_staff.py
	coverage3 report -m --skip-covered

docs:
	@echo "===== Docs ====="
	pdoc3 --force --html -o doc/ brain/ tests/

pipupdate:
	pip --disable-pip-version-check list --outdated --format=json | python -c "import json, sys; print('\n'.join([x['name'] for x in json.load(sys.stdin)]))" | xargs -n1 pip install -U
