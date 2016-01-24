REQUIREMENTS="requirements-dev.txt"

all: test

uninstall-keedi:
	@echo Removing existing installation of keedi
	- pip uninstall --yes keedi >/dev/null
	! which keedi
	@echo

uninstall-all: uninstall-keedi
	- pip uninstall --yes -r $(REQUIREMENTS)

init: uninstall-keedi
	@echo Installing dev requirements
	pip install --upgrade -r $(REQUIREMENTS)
	@echo Installing Keedi(END)
	pip install --upgrade --editable .
	@echo

test: init
	@echo Running tests in on current Python with coverage 
	py.test --cov-report term-missing --cov ./keedi --verbose ./tests
	@echo