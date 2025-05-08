all: test cover lint

test:
	#PYTHONPATH=. py.test tests
	python3 -m pytest tests/*.py

cover:
	coverage3 erase
	PYTHONPATH=. coverage3 run --branch --omit=tests/\* tests/test_spelllistprepared.py
	PYTHONPATH=. coverage3 run --branch --omit=tests/\* tests/test_spell.py
	PYTHONPATH=. coverage3 run --branch --omit=tests/\* tests/test_spelltriggergesture.py
	PYTHONPATH=. coverage3 run --branch --omit=tests/\* tests/test_spelltrigger.py
	PYTHONPATH=. coverage3 run --branch --omit=tests/\* tests/test_staffevent.py
	PYTHONPATH=. coverage3 run --branch --omit=tests/\* tests/test_staff.py
	coverage3 report -m --skip-covered

# python3 -m pip install pylint --user
lint:
	pylint *.py const/*.py tests/*.py

# pip3 install pycodestyle
pycodestyle:
	pycodestyle *.py const/*.py tests/*.py

# pip3 install mypy --user
mypy:
	mypy *.py const/*.py tests/*.py

