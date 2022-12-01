package main

import "testing"

func Test_partOne(t *testing.T) {
	want := 24000
	got := partOne()

	if want != got {
		t.Errorf("partOne() => got %v, want %v", got, want)
	}
}

func Test_partTwo(t *testing.T) {
	want := 45000
	got := partTwo()

	if want != got {
		t.Errorf("partTwo() => got %v, want %v", got, want)
	}
}
