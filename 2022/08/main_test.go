package main

import (
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	content := util.ReadInputAsStringLines("\n")

	want := 21
	got := partOne(content)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	content := util.ReadInputAsStringLines("\n")

	want := 8
	got := partTwo(content)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}
