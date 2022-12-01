.DEFAULT_GOAL=help

clean: # Clean up cached files
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

help: # Show this help
	@echo
	@echo -e "\033[0;32m Advent of Code (aoc) \033[0m"
	@echo
	@grep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf " \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

py-bootstrap: # Install necessary python dependencies to run cli
	@poetry install

py-flint: clean # Run formatters and linters
	@poetry run black .
	@poetry run isort .
	@poetry run mypy ./aoc

py-solve: # Solve problem for given year and day in Python
	@echo
	@echo -e "\033[0;32mAdvent of Code Year $(year) Day $(day) (Python)\033[0m"
	@echo
	@poetry run python ./$(year)/$(day)/main.py
