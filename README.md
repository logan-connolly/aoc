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

# Install package

Make sure you have [poetry](https://python-poetry.org/) installed on your system.

Then you can run `$ poetry install` in the project root to install all dependencies.

# Get solutions

Once you have everything installed, you can launch interactive shell with `$ poetry shell`. Once shell is activated, you can retrieve answers to questions using the following syntax:

```python
# To get individual day
$ python -m aoc -y 2020 -d 1

# To get all results for year
$ python -m aoc -y 2020
```

You can also run all the unit tests by running:

```python
$ pytest aoc
```
