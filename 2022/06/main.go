package main

import (
	"fmt"

	"github.com/logan-connolly/aoc/internal/util"
)

const (
	StartOfPacketMarker  = 4
	StartOfMessageMarker = 14
)

func main() {
	content := util.ReadInputAsString()

	p1 := partOne(content)
	p2 := partTwo(content)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(content string) int {
	return solve(content, 0, StartOfPacketMarker)
}

func partTwo(content string) int {
	return solve(content, 0, StartOfMessageMarker)
}

func solve(content string, index int, marker int) int {
	subset := []rune(content[:marker])

	if len(subset) == len(util.ToSet(subset)) {
		return index + marker
	}

	return solve(content[1:], index+1, marker)
}
