package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, _ := os.Open("C:/Users/simon/Documents/aoc2021/d1/input.txt")
	scanner := bufio.NewScanner(file)
	depths := make([]int, 0)
	for scanner.Scan() {
		val, _ := strconv.Atoi(scanner.Text())
		depths = append(depths, val)
	}
	partOne, partTwo := 0, 0
	for i, depth := range depths[:len(depths)-1] {
		if depths[i+1] > depth {
			partOne++
		}
		windOne, windTwo := 0, 0
		if i <= len(depths)-4 {
			for _, val := range depths[i : i+3] {
				windOne += val
			}
			windTwo = windOne - depths[i] + depths[i+3]
			if windTwo > windOne {
				partTwo++
			}
		}
	}
	fmt.Printf("Solution part 1 %d, part 2 %d", partOne, partTwo)
}
