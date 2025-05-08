all: pycodestyle docs lint mypy

test:
	python3 -m *.py

cover:
	coverage3 erase
	#coverage3 run --branch --append --source=brain tests/test_spelllistprepared.py
	coverage3 report -m --skip-covered

lint:
	pylint *.py || true

pycodestyle:
	pycodestyle *.py

mypy:
	mypy *.py

docs:
	pdoc3 --force --html -o doc/ *.py
