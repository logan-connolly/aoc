package main

import (
	"fmt"
	"sort"
	"strings"

	"github.com/logan-connolly/aoc/internal/util"
)

func main() {
	data := util.ReadInputAsStringLines("\n\n")
	p1 := partOne(data)
	p2 := partTwo(data)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(data []string) int {
	calorieTotals := calculateNestedTotals(data)
	rankSortTotals(&calorieTotals)

	return calorieTotals[0]
}

func partTwo(data []string) int {
	calorieTotals := calculateNestedTotals(data)
	rankSortTotals(&calorieTotals)

	var topThreeCombined int
	for _, total := range calorieTotals[:3] {
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
			total += util.ToInt(subItemString)
		}

		totals = append(totals, total)
	}

	return totals
}

func rankSortTotals(t *[]int) {
	sort.Sort(sort.Reverse(sort.IntSlice(*t)))
}
