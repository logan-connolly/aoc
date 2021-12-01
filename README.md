# 🎄 Advent of Code (AoC)

[![tests](https://github.com/logan-connolly/aoc/actions/workflows/test.yaml/badge.svg)](https://github.com/logan-connolly/aoc/actions)

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. I chose to use python and to package the solutions into the `aoc` python package.

# Requirements

Make sure you have `python>=3.9` as well as [poetry](https://python-poetry.org/) installed on your Unix system.

# Usage

This project uses a Makefile to organize common commands like the following:

```shell
# Get help
make

# Install deps for aoc
make bootstrap

# Run tests
make test

# Get solutions for a given day
make run year=2020 day=1
```
