package main

import (
	"reflect"
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	content := util.ReadInputAsString()

	want := "CMZ"
	got := partOne(content)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	content := util.ReadInputAsString()

	want := "MCD"
	got := partTwo(content)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}

func Test_extractCommands(t *testing.T) {
	content := util.ReadInputAsString()

	want := []Command{
		{qty: 1, from: 2, to: 1}, // move 1 from 2 to 1
		{qty: 3, from: 1, to: 3}, // move 3 from 1 to 3
		{qty: 2, from: 2, to: 1}, // move 2 from 2 to 1
		{qty: 1, from: 1, to: 2}, // move 1 from 1 to 2
	}
	got := extractCommands(content)

	if !reflect.DeepEqual(want, got) {
		t.Errorf("got %v, want %v", got, want)
	}
}
