package main

import (
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	p1 := partOne()
	p2 := partTwo()

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne() int {
	data := ReadInputAsString()
	elfItems := strings.Split(data, "\n\n")

	CalorieTotals := calculateNestedTotals(elfItems)
	rankedCalorieTotals := rankTotals(CalorieTotals)

	return rankedCalorieTotals[0]
}

func partTwo() int {
	data := ReadInputAsString()
	elfItems := strings.Split(data, "\n\n")

	calorieTotals := calculateNestedTotals(elfItems)
	rankedCalorieTotals := rankTotals(calorieTotals)

	var topThreeCombined int
	for _, total := range rankedCalorieTotals[:3] {
		topThreeCombined += total
	}
	return topThreeCombined
}

func calculateNestedTotals(items []string) []int {
	totals := []int{}
	for _, itemString := range items {
		subItems := strings.Split(itemString, "\n")

		var total int
		for _, subItemString := range subItems {
			total += CastToInt(subItemString)
		}

		totals = append(totals, total)
	}

	return totals
}

func rankTotals(t []int) []int {
	sort.Slice(t, func(i, j int) bool {
		return t[i] > t[j]
	})
	return t
}

// CastToInt is a helper function for casting string values
// to base 10 integers.
func CastToInt(s string) int {
	number, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}
	return number
}

// ReadInputAsString is a helper function for reading in the
// problem input and converting it to string.
func ReadInputAsString() string {
	content, err := os.ReadFile("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	return strings.TrimRight(string(content[:]), "\n")
}