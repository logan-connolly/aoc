package util

// Split takes a slice and splits it into two. The caller
// can specify a `ratio` parameter to change the lengths
// of each split
func Split[T any](s []T, ratio float64) ([]T, []T) {
	sliceLength := float64(len(s))
	midpoint := int(sliceLength * ratio)
	return s[:midpoint], s[midpoint:]
}

// Contains takes a slice and a value and returns true
// if it exists, else false.
func Contains[T Comparable](s []T, value T) bool {
	for _, item := range s {
		if item == value {
			return true
		}
	}
	return false
}

// FindMatches iterates through the items in the shorter
// slice and returns all the matches that it finds.
func FindMatches[T Comparable](s1, s2 []T) []T {
	if len(s2) < len(s1) {
		s1, s2 = s2, s1
	}

	matchSet := make(map[T]bool)
	for _, item := range s1 {
		_, exists := matchSet[item]
		if !exists && Contains(s2, item) {
			matchSet[item] = true
		}
	}

	return KeysToSlice(matchSet)
}
