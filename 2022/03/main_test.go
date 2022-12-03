package main

import (
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	data := util.ReadInputAsStringLines("\n")

	want := 157
	got := partOne(data)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	data := util.ReadInputAsStringLines("\n")

	want := 70
	got := partTwo(data)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}

func Test_getPriority(t *testing.T) {
	tests := []struct {
		input rune
		want  int
	}{
		{input: 'a', want: 1},
		{input: 'z', want: 26},
		{input: 'A', want: 27},
		{input: 'Z', want: 52},
	}
	for _, tt := range tests {
		got := getPriority(tt.input)
		if tt.want != got {
			t.Fatalf("expected: %v, got: %v", tt.want, got)
		}
	}
}
