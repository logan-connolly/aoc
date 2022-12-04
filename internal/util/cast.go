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

// ToSet takes a slice as input and outputs a set.
func ToSet[T comparable](s []T) map[T]bool {
	setMap := make(map[T]bool)
	for _, item := range s {
		setMap[item] = true
	}
	return setMap
}

// KeysToSlice converts map keys into a slice.
func KeysToSlice[K comparable, V any](m map[K]V) []K {
	keys := make([]K, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	return keys
}
