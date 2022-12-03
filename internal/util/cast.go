package util

import (
	"log"
	"strconv"
)

// ToInt is a helper function for casting string values
// to base 10 integers.
func ToInt(s string) int {
	number, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}
	return number
}

// KeysToSlice converts map keys into a slice.
func KeysToSlice[K Comparable, V any](m map[K]V) []K {
	keys := make([]K, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	return keys
}
