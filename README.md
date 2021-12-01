# Advent of Code (AoC)

<p>
<a href="https://travis-ci.com/github/logan-connolly/aoc">
    <img src="https://travis-ci.com/logan-connolly/aoc.svg?branch=main" alt="Build Status">
</a>
<a href="https://codecov.io/gh/logan-connolly/aoc">
  <img src="https://codecov.io/gh/logan-connolly/aoc/branch/main/graph/badge.svg?token=K8WVXKIDY6"/>
</a>
</p>

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. I chose to use python and to package the solutions into the `aoc` python package.

# Requirements

Make sure you have `python>=3.9` as well as [poetry](https://python-poetry.org/) installed on your Unix system.

# Usage

This project uses a Makefile to organize common commands

```shell
# Get help
make

# Install deps for aoc
make bootstrap

# Run tests
make test

# Get solutions for a given year
make run year=2020

# Get solutions for a given day
make run year=2020 day=1
```
