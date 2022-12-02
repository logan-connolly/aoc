package main

import (
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	data := util.ReadInputAsStringLines("\n\n")

	want := 24000
	got := partOne(data)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	data := util.ReadInputAsStringLines("\n\n")

	want := 45000
	got := partTwo(data)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}
