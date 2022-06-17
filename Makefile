all: install

install:
	python setup.py install

local:
	python setup.py install --user

test:
	python -m pytest --cov-report html --cov=myutils --cov-branch tests
