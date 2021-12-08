package aocutils

import (
	"bufio"
	"fmt"
	"os"
)

func ReadLines() []string {
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

func PrintSolutions(sols ...int) {
	fmt.Printf("Solutions: ")
	for _, sol := range sols {
		fmt.Println(sol)
	}
}
