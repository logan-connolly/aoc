package main

import (
	"fmt"

	"github.com/logan-connolly/aoc/internal/util"
)

func main() {
	lines := util.ReadInputAsStringLines("\n")
	p1 := partOne(lines)
	p2 := partTwo(lines)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(lines []string) int {
	var total int
	for _, line := range lines {
		s1, s2 := util.Split([]rune(line), 0.5)
		matches := findMatches(s1, s2)
		total += getPriority(matches[0])
	}
	return total
}

func partTwo(lines []string) int {
	var total int
	for _, g := range makeGroups(lines) {
		e1, e2, e3 := []rune(g[0]), []rune(g[1]), []rune(g[2])

		e1e2 := findMatches(e1, e2)
		e1e3 := findMatches(e1, e3)

		if matches := findMatches(e1e2, e1e3); len(matches) == 1 {
			total += getPriority(matches[0])
		}
	}
	return total
}

// makeGroups takes the raw input lines and groups them
// into groups of three elves.
func makeGroups(lines []string) [][]string {
	var groups [][]string
	var group []string

	for _, line := range lines {
		switch len(group) {
		case 2:
			group = append(group, line)
			groups = append(groups, group)
			group = make([]string, 0)
		default:
			group = append(group, line)
		}
	}
	return groups
}

// findMatches iterates through the two compartments of items
// and returns the matched item when found.
func findMatches(s1, s2 []rune) []rune {
	matchSet := make(map[rune]bool)
	for _, item := range s1 {
		_, exists := matchSet[item]
		if !exists && util.Contains(s2, item) {
			matchSet[item] = true
		}
	}
	return util.KeysToSlice(matchSet)
}

// getPriority takes a rune character (rucksack item) and
// returns the item priority (a=1, b=2, ..., Z=52).
func getPriority(code rune) int {
	charValue := int(code)
	if charValue < 97 {
		return charValue - 38 // upper case
	}
	return charValue - 96 // lower case
}
