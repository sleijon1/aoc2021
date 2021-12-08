package main

import (
	"strconv"

	"github.com/sleijon1/aoc2021/aocutils"
)

var flip = map[byte]string{'0': "1", '1': "0"}

func most_com(bit_i int, bits_list []string) string {
	occ := map[byte]int{'0': 0, '1': 0}
	var bit_rows int = len(bits_list)
	for i := 0; i < bit_rows; i++ {
		occ[bits_list[i][bit_i]] += 1
	}
	if occ['0'] > occ['1'] {
		return "0"
	} else {
		return "1"
	}
}

func part_1(instructions []string) int64 {
	var gamma string = ""
	var eps string = ""
	var bits int = len(instructions[0])
	for i := 0; i < bits; i++ {
		gamma += most_com(i, instructions)
	}
	for _, char := range gamma {
		eps += flip[byte(char)]
	}
	gammaInt, _ := strconv.ParseInt(gamma, 2, 64)
	epsInt, _ := strconv.ParseInt(eps, 2, 64)
	return gammaInt * epsInt
}

func main() {
	lines := aocutils.ReadLines()
	aocutils.PrintSolutions(int(part_1(lines)))
}
