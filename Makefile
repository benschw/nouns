
.DEFAULT_GOAL := help
help: ## Show this help
	@sed -e '/^[a-zA-Z0-9_\-]*:.*##/!d' -e 's/:.*##\s*/:/' \
		$(MAKEFILE_LIST) | sort | column -c2 -t -s :

check: lint test-cov

##################################
install: ## Install project dependencies
	poetry install -v

remove-env:
	poetry env remove --all

install-clean: remove-env install ## Uninstall then reinstall project dependencies

update-lock:
	poetry lock

update-deps: update-lock install ## Update the dependencies in the lockfile and install

lint: mypy ## Run pre-commit linting
	poetry run pre-commit run --all-files

test: ## Run repo tests
	poetry run pytest tests

test-cov:
	poetry run pytest --cov --cov-report html --cov-report xml tests

mypy: ## Run mypy to detect type hinting errors
	poetry run mypy authz


process: ## process training data and input files to generate output nouns
	python3 nouns/main.py process

three-nouns: ## print 1 abstract & 2 concrete nouns
	python3 nouns/main.py three-nouns