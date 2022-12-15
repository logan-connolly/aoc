package main

import (
	"fmt"
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
	outputs := getStrengthOutputs(lines)
	return getSignalStrength(outputs)
}

func partTwo(lines []string) int {
	// TODO: not completed
	return -1
}

func getStrengthOutputs(lines []string) (outputs []int) {
	register := 1
	for _, input := range lines {
		if strings.Contains(input, "noop") {
			outputs = append(outputs, register)
		} else {
			outputs = append(outputs, []int{register, register}...)
			tokens := strings.Split(input, " ") // ie. "addx -1"
			register += util.ToInt(tokens[1])
		}
	}
	return outputs
}

func getSignalStrength(outputs []int) (signal int) {
	for i, op := range outputs {
		switch cycle := i + 1; cycle {
		case 20, 60, 100, 140, 180, 220:
			signal += cycle * op
		default:
			continue
		}
	}
	return signal
}
