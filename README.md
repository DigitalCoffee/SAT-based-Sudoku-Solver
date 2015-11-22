# SAT-based-Sudoku-Solver
Converts an input string to DIMACS format to be run through miniSAT. The output of miniSAT is parsed an a solution is prettyprinted.

## Requirements

* Python 3
* [Minisat](http://minisat.se/MiniSat.html)

## Using

* `make` for a normal run on a default puzzle.
* `make extended` to use the extended rule set.
* `make hard` to run on a "hard" problem.
* `make unsolvable` to run on an unsolvable problem.
