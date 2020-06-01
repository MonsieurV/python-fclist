install:
	pipenv install

install-dev:
	pipenv install --dev

test:
	pipenv run pytest -vv

install-package-in-venv:
	pipenv uninstall fclist
	pipenv run python setup.py install

test-package-in-venv: install-package-in-venv test

format:
	pipenv run black .
