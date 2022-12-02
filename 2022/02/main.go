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
		other := ActionInfoMap[rawOther]
		self := getActionInfoFromEncryption(rawSelf)

		round := NewRound(other, self)
		scores = append(scores, round.GetScore())
	}

	return util.SumInts(scores)
}

func partTwo(lines []string) int {
	var scores []int
	for _, rawRoundInput := range lines {
		rawOther, rawSelf := getRawSigns(rawRoundInput)
		other := ActionInfoMap[rawOther]
		self := getActionInfoFromCommand(rawSelf, other)

		round := NewRound(other, self)
		scores = append(scores, round.GetScore())
	}

	return util.SumInts(scores)
}

func getRawSigns(s string) (string, string) {
	rawSigns := strings.Split(s, " ")
	return rawSigns[0], rawSigns[1]
}

type ActionInfo struct {
	sign  string
	beats string
	loses string
	value int
}

var ActionInfoMap = map[string]ActionInfo{
	Rock:     {Rock, Scissors, Paper, 1},
	Paper:    {Paper, Rock, Scissors, 2},
	Scissors: {Scissors, Paper, Rock, 3},
}

func getActionInfoFromEncryption(s string) ActionInfo {
	switch s {
	case "X":
		return ActionInfoMap[Rock]
	case "Y":
		return ActionInfoMap[Paper]
	case "Z":
		return ActionInfoMap[Scissors]
	default:
		log.Fatal("Did not recognize the encrypted sign provided:", s)
		return ActionInfo{}
	}
}

func getActionInfoFromCommand(s string, other ActionInfo) ActionInfo {
	switch s {
	case "X":
		return ActionInfoMap[other.beats]
	case "Y":
		return ActionInfoMap[other.sign]
	case "Z":
		return ActionInfoMap[other.loses]
	default:
		log.Fatal("Did not recognize the encrypted sign provided:", s)
		return ActionInfo{}
	}
}

type Round struct {
	other ActionInfo
	self  ActionInfo
}

func NewRound(other, self ActionInfo) Round {
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
