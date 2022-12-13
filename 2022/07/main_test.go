package main

import (
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	lines := util.ReadInputAsStringLines("\n")

	want := 95437
	got := partOne(lines)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	lines := util.ReadInputAsStringLines("\n")

	want := 24933642
	got := partTwo(lines)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}
