#!/bin/bash

YEAR=$1
DAY=$2
SRC_PATH=aoc/year_${YEAR}/day_${DAY}
RESOURCES=aoc/year_${YEAR}/resources
TEST_PATH=aoc/tests/year_${YEAR}

mkdir -p $SRC_PATH
mkdir -p $TEST_PATH

touch $SRC_PATH/__init__.py
touch $SRC_PATH/part_one.py
touch $SRC_PATH/part_two.py

touch $TEST_PATH/test_day_${DAY}.py
touch $RESOURCES/day_${DAY}.txt
