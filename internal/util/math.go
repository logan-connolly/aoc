package util

// SumInts sums a slice of integers.
func SumInts(ns []int) int {
	var total int
	for _, n := range ns {
		total += n
	}

	return total
}
