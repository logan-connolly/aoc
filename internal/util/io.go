package util

import (
	"log"
	"os"
	"strings"
)

// ReadInputAsString is a helper function for reading in the
// problem input and converting it to string.
func ReadInputAsString() string {
	content, err := os.ReadFile("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	return strings.TrimRight(string(content[:]), "\n")
}

// ReadInputAsStringLines is a helper function for reading in the
// problem input and converting it to a slice of strings.
func ReadInputAsStringLines(delim string) []string {
	s := ReadInputAsString()
	return strings.Split(s, delim)
}
