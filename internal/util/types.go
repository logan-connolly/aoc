package util

// Comparable type interface specifies types that we can
// compare against each other.
type Comparable interface {
	int64 | float64 | string | rune
}
