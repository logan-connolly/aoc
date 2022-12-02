package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/logan-connolly/aoc/internal/util"
)

const (
	Rock     string = "A"
	Paper    string = "B"
	Scissors string = "C"
	Loss     int    = 0
	Draw     int    = 3
	Win      int    = 6
)

func main() {
	lines := util.ReadInputAsStringLines("\n")
	p1 := partOne(lines)
	p2 := partTwo(lines)

	fmt.Printf("Solutions(p1=%d, p2=%d)", p1, p2)
}

func partOne(lines []string) int {
	var scores []int
	for _, rawRoundInput := range lines {
		rawOther, rawSelf := getRawSigns(rawRoundInput)
		other := ActionMap[rawOther]
		self := getActionFromEncryption(rawSelf)

		round := NewRound(other, self)
		scores = append(scores, round.GetScore())
	}

	return util.SumInts(scores)
}

func partTwo(lines []string) int {
	var scores []int
	for _, rawRoundInput := range lines {
		rawOther, rawSelf := getRawSigns(rawRoundInput)
		other := ActionMap[rawOther]
		self := getActionFromCommand(rawSelf, other)

		round := NewRound(other, self)
		scores = append(scores, round.GetScore())
	}

	return util.SumInts(scores)
}

func getRawSigns(s string) (string, string) {
	rawSigns := strings.Split(s, " ")
	return rawSigns[0], rawSigns[1]
}

type Action struct {
	sign  string
	beats string
	loses string
	value int
}

var ActionMap = map[string]Action{
	Rock:     {Rock, Scissors, Paper, 1},
	Paper:    {Paper, Rock, Scissors, 2},
	Scissors: {Scissors, Paper, Rock, 3},
}

func getActionFromEncryption(s string) Action {
	switch s {
	case "X":
		return ActionMap[Rock]
	case "Y":
		return ActionMap[Paper]
	case "Z":
		return ActionMap[Scissors]
	default:
		log.Fatal("Did not recognize the encrypted sign provided:", s)
		return Action{}
	}
}

func getActionFromCommand(s string, other Action) Action {
	switch s {
	case "X":
		return ActionMap[other.beats]
	case "Y":
		return ActionMap[other.sign]
	case "Z":
		return ActionMap[other.loses]
	default:
		log.Fatal("Did not recognize the encrypted sign provided:", s)
		return Action{}
	}
}

type Round struct {
	other Action
	self  Action
}

func NewRound(other, self Action) Round {
	return Round{other, self}
}

func (r *Round) GetScore() int {
	switch r.other.sign {
	case r.self.sign:
		return Draw + r.self.value
	case r.self.beats:
		return Win + r.self.value
	case r.self.loses:
		return Loss + r.self.value
	default:
		log.Fatal("Did not recognize the sign provided:", r.other.sign)
		return -1
	}
}
