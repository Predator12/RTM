ENV = env

PYBIN = $(ENV)/scripts
PYTHON = $(PYBIN)/python
PIP = $(PYBIN)/pip

.PHONY: help
help:
	@echo "make environ                   # initialize environment"

.PHONY: environ
environ: clean requirements.txt
	virtualenv $(ENV)
	$(PIP) install -r requirements-dev.txt
	@if not exist ./tmp mkdir tmp
	@echo "initialization complete"

