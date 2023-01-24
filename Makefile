.DEFAULT_GOAL=help

help: # Show this help
	@echo
	@echo -e "\033[0;32m Advent of Code (aoc) \033[0m"
	@echo
	@grep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf " \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

go-test: # Run the tests for each solution
	@go test ./...

py-utils: # Install py utils
	@pip install git+https://github.com/logan-connolly/aoc-python-utils@v1.0.1

py-solve: # Solve problem for given year and day in Python
	@echo
	@echo -e "\033[0;32mAdvent of Code Year $(year) Day $(day) (Python)\033[0m"
	@echo
	@python ./$(year)/$(day)/main.py
