package util

import (
	"reflect"
	"testing"
)

func Test_Split(t *testing.T) {
	tests := []struct {
		input     []string
		ratio     float64
		wantLeft  []string
		wantRight []string
	}{
		{
			input:     []string{"a", "b"},
			ratio:     0.5,
			wantLeft:  []string{"a"},
			wantRight: []string{"b"},
		},
		{
			input:     []string{"a", "b", "c", "d"},
			ratio:     0.25,
			wantLeft:  []string{"a"},
			wantRight: []string{"b", "c", "d"},
		},
		{
			input:     []string{"a", "b", "c", "d"},
			ratio:     0.75,
			wantLeft:  []string{"a", "b", "c"},
			wantRight: []string{"d"},
		},
	}
	for _, tt := range tests {
		left, right := Split(tt.input, tt.ratio)
		if !reflect.DeepEqual(tt.wantLeft, left) {
			t.Fatalf("expected: %v, got: %v on the left side", tt.wantLeft, left)
		}
		if !reflect.DeepEqual(tt.wantRight, right) {
			t.Fatalf("expected: %v, got: %v on the right side", tt.wantRight, right)
		}
	}
}
