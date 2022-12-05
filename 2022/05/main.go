package main

import (
	"fmt"
	"strings"
	"unicode"

	"github.com/logan-connolly/aoc/internal/util"
)

func main() {
	content := util.ReadInputAsString()

	p1 := partOne(content)
	p2 := partTwo(content)

	fmt.Printf("Solutions(p1=%s, p2=%s)", p1, p2)
}

func partOne(content string) string {
	stacks := extractStacks(content)
	commands := extractCommands(content)

	for _, cmd := range commands {
		var rest []string
		var items []string

		rest = append(rest, stacks[cmd.from][cmd.qty:]...)
		items = append(items, stacks[cmd.from][:cmd.qty]...)
		util.Reverse(items)

		stacks[cmd.from] = rest
		stacks[cmd.to] = append(items, stacks[cmd.to]...)
	}

	return getMessage(stacks)
}

func partTwo(content string) string {
	stacks := extractStacks(content)
	commands := extractCommands(content)

	for _, cmd := range commands {
		var rest []string
		var items []string

		rest = append(rest, stacks[cmd.from][cmd.qty:]...)
		items = append(items, stacks[cmd.from][:cmd.qty]...)

		stacks[cmd.from] = rest
		stacks[cmd.to] = append(items, stacks[cmd.to]...)
	}

	return getMessage(stacks)
}

// getMessage builds the string by taking the first element
// of each character stack.
func getMessage(stacks map[int][]string) string {
	chars := make([]string, 0)
	for i := 0; i < len(stacks); i++ {
		topOfStack := stacks[i+1][0]
		chars = append(chars, topOfStack)
	}

	return strings.Join(chars[:], "")
}

// extractStacks iterates over the depicted stacks, building
// up a stack map which will be used to operate on via
// commands.
func extractStacks(rawInput string) map[int][]string {
	stackMap := make(map[int][]string)
	rawStacks := strings.Split(rawInput, "\n\n")[0]

	for _, line := range strings.Split(rawStacks, "\n") {
		var stackIdx int
		for i := 1; i < len(line); i += 4 {
			stackIdx++
			if crate := line[i]; unicode.IsLetter(rune(crate)) {
				stackMap[stackIdx] = append(stackMap[stackIdx], string(crate))
			}
		}
	}
	return stackMap
}

// Command provides the information necessary to perform
// an operation on the stack.
type Command struct {
	qty  int
	from int
	to   int
}

// extractCommands iterates over the raw commands and casts
// them to the Command struct type.
func extractCommands(rawInput string) []Command {
	var commands []Command
	rawCommands := strings.Split(rawInput, "\n\n")[1]

	for _, rc := range strings.Split(rawCommands, "\n") {
		var qty, from, to int
		fmt.Sscanf(rc, "move %d from %d to %d", &qty, &from, &to)
		commands = append(commands, Command{qty, from, to})
	}
	return commands
}
