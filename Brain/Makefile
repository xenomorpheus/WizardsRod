all: test cover lint mypy checkstyle doco

test:
	PYTHONPATH=src python3 -m pytest tests/*.py

cover:
	coverage3 erase
	PYTHONPATH=src coverage3 run --branch --omit=tests/\* tests/test_spelllistprepared.py
	PYTHONPATH=src coverage3 run --branch --omit=tests/\* tests/test_spell.py
	PYTHONPATH=src coverage3 run --branch --omit=tests/\* tests/test_spelltriggergesture.py
	PYTHONPATH=src coverage3 run --branch --omit=tests/\* tests/test_spelltrigger.py
	PYTHONPATH=src coverage3 run --branch --omit=tests/\* tests/test_staffevent.py
	PYTHONPATH=src coverage3 run --branch --omit=tests/\* tests/test_staff.py
	coverage3 report -m --skip-covered

lint:
	pylint src/ tests/

pycodestyle:
	pycodestyle src/ tests/

mypy:
	mypy src/ tests/

doco:
	PYTHONPATH=src pdoc3 --html -o doc/ src/ tests/
