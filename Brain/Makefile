all: autoformat pycodestyle lint mypy test cover docs


autoformat:
	@echo "===== autoformat ====="
	black --line-length=120  brain/ tests/


test:
	python3 --version
	python3 -m pytest tests/*.py

cover:
	coverage3 erase
	coverage3 run --branch --append --source=brain tests/test_spelllistprepared.py
	coverage3 run --branch --append --source=brain tests/test_spell.py
	coverage3 run --branch --append --source=brain tests/test_spelltriggergesture.py
	coverage3 run --branch --append --source=brain tests/test_spelltrigger.py
	coverage3 run --branch --append --source=brain tests/test_staffevent.py
	coverage3 run --branch --append --source=brain tests/test_staff.py
	coverage3 report -m --skip-covered

lint:
	@echo "===== Lint ====="
	pylint brain/ tests/ || true

pycodestyle:
	@echo "===== pycodestyle ====="
	pycodestyle --max-line-length=120 brain/ tests/

mypy:
	@echo "===== MyPy ====="
	mypy brain/ tests/ || true

docs:
	@echo "===== Docs ====="
	pdoc3 --force --html -o doc/ brain/ tests/

pipupdate:
	pip --disable-pip-version-check list --outdated --format=json | python -c "import json, sys; print('\n'.join([x['name'] for x in json.load(sys.stdin)]))" | xargs -n1 pip install -U