all: test cover lint mypy checkstyle doco

test:
	PYTHONPATH=brain python3 -m pytest tests/*.py

cover:
	coverage3 erase
	PYTHONPATH=brain coverage3 run --branch --omit=tests/\* tests/test_spelllistprepared.py
	PYTHONPATH=brain coverage3 run --branch --omit=tests/\* tests/test_spell.py
	PYTHONPATH=brain coverage3 run --branch --omit=tests/\* tests/test_spelltriggergesture.py
	PYTHONPATH=brain coverage3 run --branch --omit=tests/\* tests/test_spelltrigger.py
	PYTHONPATH=brain coverage3 run --branch --omit=tests/\* tests/test_staffevent.py
	PYTHONPATH=brain coverage3 run --branch --omit=tests/\* tests/test_staff.py
	coverage3 report -m --skip-covered

lint:
	pylint brain/ tests/

pycodestyle:
	pycodestyle brain/ tests/

mypy:
	mypy brain/ tests/

doco:
	PYTHONPATH=brain pdoc3 --html -o doc/ brain/ tests/
