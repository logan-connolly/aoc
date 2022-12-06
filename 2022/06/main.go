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
	return solve([]rune(content), StartOfPacketMarker, 0)
}

func partTwo(content string) int {
	return solve([]rune(content), StartOfMessageMarker, 0)
}

func solve(chars []rune, marker, index int) int {
	if len(chars[:marker]) == len(util.ToSet(chars[:marker])) {
		return marker + index
	}
	return solve(chars[1:], marker, index+1)
}
