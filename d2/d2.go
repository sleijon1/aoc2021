package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readLines() []string {
	wd, _ := os.Getwd()
	read := wd + "\\input.txt"
	file, _ := os.Open(read)
	scanner := bufio.NewScanner(file)
	lines := make([]string, 0)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func main() {
	lines := readLines()
	m := make(map[string]int)
	for i := 0; i < len(lines); i++ {
		split := strings.Fields(lines[i])
		cmd := split[0]
		val, _ := strconv.Atoi(split[1])
		switch cmd {
		case "forward":
			m["pos"] += val
			m["depth"] += m["aim"] * val
		case "up":
			m["aim"] -= val
		case "down":
			m["aim"] += val
		}
	}
	fmt.Printf("Solution part 1 %d, part 2 %d", m["aim"]*m["pos"], m["depth"]*m["pos"])
}
