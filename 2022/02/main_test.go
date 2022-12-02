package main

import (
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	data := util.ReadInputAsStringLines("\n")

	want := 15
	got := partOne(data)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	data := util.ReadInputAsStringLines("\n")

	want := 12
	got := partTwo(data)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}
