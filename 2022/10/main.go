package main

import (
	"fmt"
	"strings"

	"github.com/logan-connolly/aoc/internal/util"
)

func main() {
	lines := util.ReadInputAsStringLines("\n")

	fmt.Printf("Solutions(p1=%d)\n", partOne(lines))
	partTwo(lines)
}

func partOne(lines []string) int {
	outputs := getStrengthOutputs(lines)
	return getSignalStrength(outputs)
}

func partTwo(lines []string) {
	outputs := getStrengthOutputs(lines)
	displayLetters(outputs)
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

func getCharacter(idx, output int) string {
	switch idx - output {
	case -1, 0, 1:
		return "#"
	default:
		return "."
	}
}

func displayLetters(outputs []int) (signal int) {
	for idx, output := range outputs {
		char := getCharacter(idx%40, output)
		switch (idx + 1) % 40 {
		case 0:
			fmt.Println(char)
		default:
			fmt.Print(char)
		}
	}
	return signal
}
