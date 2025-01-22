.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Sets up the local environment (e.g. install git hooks)
	scripts/local-setup.sh
	make install

.PHONY: up
up: ## Run Streamlit app
	 poetry run streamlit run main.py --server.port=8501 --server.address=0.0.0.0

.PHONY: install
install: ## Install the app packages
	 rm -rf poetry.lock
	 poetry install --no-root

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-lint
check-lint: ## Checks the code style
	poetry run ruff check

.PHONY: lint
lint: ## Lints the code format
	poetry run ruff check --fix

.PHONY: check-format
check-format:  ## Check format python code
	poetry run ruff format --check

.PHONY: format
format:  ## Format python code
	poetry run ruff format

.PHONY: test-unit
test-unit: ## Run unit the tests
	 PYTHONPATH=. poetry run pytest -n auto tests/unit -ra

.PHONY: test-integration
test-integration: ## Run integration the tests
	 PYTHONPATH=. poetry run pytest -n auto tests/integration -ra

.PHONY: test-acceptance
test-acceptance: ## Run acceptance the tests
	 PYTHONPATH=. poetry run pytest -n auto tests/acceptance -ra

.PHONY: test
test: test-unit test-integration test-acceptance ## Run all the tests

.PHONY: watch
watch: ## Run all the tests in watch mode
	 PYTHONPATH=. poetry run ptw --runner "pytest -n auto tests -ra" 

.PHONY: pre-commit
pre-commit: check-format check-typing test
