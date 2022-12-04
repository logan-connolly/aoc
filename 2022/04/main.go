package main

import (
	"fmt"
	"reflect"
	"strings"

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
		ranges := strings.Split(line, ",")
		r1, r2 := toRange(ranges[0]), toRange(ranges[1])
		s1, s2 := util.ToSet(r1), util.ToSet(r2)

		if overlapsCompletely(s1, s2) {
			total++
		}
	}
	return total
}

func partTwo(lines []string) int {
	var total int
	for _, line := range lines {
		ranges := strings.Split(line, ",")
		r1, r2 := toRange(ranges[0]), toRange(ranges[1])
		s1, s2 := util.ToSet(r1), util.ToSet(r2)

		if overlapsPartially(s1, s2) {
			total++
		}
	}
	return total
}

func toRange(raw string) []int {
	bounds := strings.Split(raw, "-")
	min, max := util.ToInt(bounds[0]), util.ToInt(bounds[1])

	var output []int
	for i := min; i <= max; i++ {
		output = append(output, i)
	}

	return output
}

func overlapsCompletely(s1, s2 map[int]bool) bool {
	if len(s2) < len(s1) {
		s1, s2 = s2, s1
	}
	return reflect.DeepEqual(s1, util.Intersect(s1, s2))
}

func overlapsPartially(s1, s2 map[int]bool) bool {
	union := util.Union(s1, s2)
	return len(union) != len(s1)+len(s2)
}
