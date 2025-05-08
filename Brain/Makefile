all: test cover lint mypy checkstyle docs

test:
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
	pylint brain/ tests/

pycodestyle:
	pycodestyle brain/ tests/

mypy:
	mypy brain/ tests/

docs:
	pdoc3 --force --html -o doc/ brain/ tests/
