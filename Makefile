
default:
	echo "TODO"

init:
	# TODO remove --user
	pip3 install --user -r requirements.txt
	# TODO where to put modules required for development?
	pip3 install --user -r requirements_development.txt
test:
	py.test brain/tests

.PHONY: init test
