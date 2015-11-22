#! /bin/env python
import sys

# Open the file to write the output
satisfiable = input()

if satisfiable == "SAT":
    print("Satisfiable")

    matrix = []

    accepted = []
    for val in input().split(" "):
        val = int(val)
        if val > 0:
            accepted.append(val)

    line = []
    for row in range(1, 10):
        for col in range(1, 10):
            x = accepted.pop(0)
            val = (-9*col)+x+(90-(81*row))
            line.append(str(val))
            if len(line) >= 9:
                matrix.append(line)
                line = []

    for row in matrix:
        print("".join(row))

else:
    print("Unsatisfiable")
