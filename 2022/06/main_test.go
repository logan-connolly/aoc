package main

import (
	"testing"

	"github.com/logan-connolly/aoc/internal/util"
)

func Test_partOne(t *testing.T) {
	content := util.ReadInputAsString()

	want := 7
	got := partOne(content)

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	content := util.ReadInputAsString()

	want := 19
	got := partTwo(content)

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}

func Test_solve(t *testing.T) {
	tests := []struct {
		input  string
		want   int
		marker int
	}{
		{input: "mjqjpqmgbljsphdztnvjfqwrcgsmlb", want: 7, marker: StartOfPacketMarker},
		{input: "bvwbjplbgvbhsrlpgdmjqwftvncz", want: 5, marker: StartOfPacketMarker},
		{input: "nppdvjthqldpwncqszvftbrmjlhg", want: 6, marker: StartOfPacketMarker},
		{input: "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", want: 10, marker: StartOfPacketMarker},
		{input: "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", want: 11, marker: StartOfPacketMarker},
		{input: "mjqjpqmgbljsphdztnvjfqwrcgsmlb", want: 19, marker: StartOfMessageMarker},
		{input: "bvwbjplbgvbhsrlpgdmjqwftvncz", want: 23, marker: StartOfMessageMarker},
		{input: "nppdvjthqldpwncqszvftbrmjlhg", want: 23, marker: StartOfMessageMarker},
		{input: "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", want: 29, marker: StartOfMessageMarker},
		{input: "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", want: 26, marker: StartOfMessageMarker},
	}

	for _, tt := range tests {
		got := solve(tt.input, 0, tt.marker)
		if got != tt.want {
			t.Errorf("solve() => got %v, want %v", got, tt.want)
		}
	}
}
