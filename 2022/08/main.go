package main

import (
	"fmt"

	"github.com/logan-connolly/aoc/internal/util"
)

func main() {
	data := util.ReadInputAsStringLines("\n")

	p1 := partOne(data)
	p2 := partTwo(data)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(data []string) (total int) {
	mapping := buildMap(data)
	upperBound := len(data) - 1

	for c := range mapping {
		if !isInvisible(mapping, c, upperBound) {
			total++
		}
	}
	return total
}

func partTwo(data []string) (bestScore int) {
	mapping := buildMap(data)
	upperBound := len(data) - 1

	for c := range mapping {
		if score := getScore(mapping, c, upperBound); score > bestScore {
			bestScore = score
		}
	}
	return bestScore
}

type Coord struct {
	x, y int
}

func buildMap(data []string) map[Coord]int {
	mapping := make(map[Coord]int)

	for ridx, row := range data {
		for cidx, char := range row {
			mapping[Coord{ridx, cidx}] = util.ToInt(string(char))
		}
	}

	return mapping
}

func isInvisible(m map[Coord]int, c Coord, upperBound int) bool {
	if c.x == 0 || c.y == 0 || c.x == upperBound || c.y == upperBound {
		return false
	}

	var west, north, east, south bool

	for x := c.x - 1; x >= 0; x-- {
		if m[Coord{x, c.y}] >= m[c] {
			west = true
		}
	}
	for x := c.x + 1; x <= upperBound; x++ {
		if m[Coord{x, c.y}] >= m[c] {
			east = true
		}
	}
	for y := c.y - 1; y >= 0; y-- {
		if m[Coord{c.x, y}] >= m[c] {
			north = true
		}
	}
	for y := c.y + 1; y <= upperBound; y++ {
		if m[Coord{c.x, y}] >= m[c] {
			south = true
		}
	}

	return west && north && east && south
}

func getScore(m map[Coord]int, c Coord, upperBound int) int {
	var west, north, east, south int

	for x := c.x - 1; x >= 0; x-- {
		west++
		if m[Coord{x, c.y}] >= m[c] {
			break
		}
	}
	for x := c.x + 1; x <= upperBound; x++ {
		east++
		if m[Coord{x, c.y}] >= m[c] {
			break
		}
	}
	for y := c.y - 1; y >= 0; y-- {
		north++
		if m[Coord{c.x, y}] >= m[c] {
			break
		}
	}
	for y := c.y + 1; y <= upperBound; y++ {
		south++
		if m[Coord{c.x, y}] >= m[c] {
			break
		}
	}

	return west * north * east * south
}
