package main

import (
	"fmt"
	"log"

	"github.com/logan-connolly/aoc/internal/util"
)

func main() {
	data := util.ReadInputAsStringLines("\n")

	p1 := partOne(data)
	p2 := partTwo(data)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(data []string) int {
	commands := parseCommands(data)
	mapping := walk(commands, 2)
	return len(mapping)
}

func partTwo(data []string) int {
	commands := parseCommands(data)
	mapping := walk(commands, 10)
	return len(mapping)
}

// Command is a movement instruction for the snake's head.
type Command struct {
	direction string
	distance  int
}

// parseCommands takes the input data and creates a sequence
// of commands to be passed to the snake walker.
func parseCommands(data []string) []Command {
	var commands []Command
	for _, rawCommand := range data {
		var direction string
		var distance int
		fmt.Sscanf(rawCommand, "%s %d", &direction, &distance)
		commands = append(commands, Command{direction, distance})
	}
	return commands
}

// Coord stores the X, Y coordinates on a 2D plane.
type Coord struct {
	x, y int
}

// Movement represents the the magnitude of which the
// the coordinate should move on the X, Y plane.
type Movement struct {
	dx, dy int
}

// abs calculates the absolute value for integers
func abs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}

// GetManhattanDistance calculates the distance between
// two points in a N dimensional vector space.
func (c *Coord) GetManhattanDistance(other Coord) int {
	if (c.x == other.x) && (c.y == other.y) {
		return 0
	}
	if abs(c.x-other.x)+abs(c.y-other.y) == 1 {
		return 1
	}
	if abs(c.x-other.x) == 1 && abs(c.y-other.y) == 1 {
		return 1
	}
	return 2
}

// Move takes a movement and updates the coordinate.
func (c *Coord) Move(m Movement) {
	if m.dx != 0 {
		c.x += m.dx / abs(m.dx)
	}
	if m.dy != 0 {
		c.y += m.dy / abs(m.dy)
	}
}

// updateTail takes the head of the knot above the
// tail and updates the tail accordingly.
func updateTail(head, tail Coord) Coord {
	if head.GetManhattanDistance(tail) <= 1 {
		// do nothing
	} else if head.x == tail.x {
		// move vertically
		tail.Move(Movement{0, head.y - tail.y})
	} else if head.y == tail.y {
		// move horizontally
		tail.Move(Movement{head.x - tail.x, 0})
	} else {
		// move diagonally
		tail.Move(Movement{head.x - tail.x, head.y - tail.y})
	}
	return tail
}

// walk takes a set of commands and a snake size and
// moves based on the command procedure passed to it.
func walk(commands []Command, snakeSize int) map[Coord]bool {
	mapping := make(map[Coord]bool)
	snake := make([]Coord, snakeSize)

	for _, cmd := range commands {
		var m Movement
		switch cmd.direction {
		case "R":
			m = Movement{1, 0}
		case "U":
			m = Movement{0, 1}
		case "L":
			m = Movement{-1, 0}
		case "D":
			m = Movement{0, -1}
		default:
			log.Fatal("Received an invalid command direction")
		}

		for i := 0; i < cmd.distance; i++ {
			// move the head
			snake[0] = Coord{snake[0].x + m.dx, snake[0].y + m.dy}

			// follow the head movement with the tail
			for i := 0; i < snakeSize-1; i++ {
				snake[i+1] = updateTail(snake[i], snake[i+1])
			}

			// mark the tip of the tail
			mapping[snake[snakeSize-1]] = true
		}
	}

	return mapping
}
