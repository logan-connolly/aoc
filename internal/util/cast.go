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
