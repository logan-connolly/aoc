.DEFAULT_GOAL=help

bootstrap: # Install necessary dependencies to run cli
	poetry install

run: # Run script for given year and [optional] day
	poetry run python -m aoc $(year) $(day)

new: # Run generate module for new day based on templates
	poetry run python -m aoc $(year) $(day) --new

test: # Run tests and coverage
	poetry run coverage run -m pytest tests
	poetry run coverage report --skip-covered
	poetry run mypy aoc

clean: # Clean up cached files
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete

help: # Show this help
	@echo
	@echo -e "\033[0;32m Advent of Code (aoc) \033[0m"
	@echo
	@echo -e "\033[0;31m > make run year=2020 day=1 \033[0m"
	@echo
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf " \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo
