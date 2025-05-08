init:
	pip3 install -r requirements.txt

test:
	py.test brain/tests

.PHONY: init test
