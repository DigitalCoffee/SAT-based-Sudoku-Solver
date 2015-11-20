print("c This is our input for the SAT solver")

print("NEED TO PUT p cnf <# variables> <# clauses> HERE")

input = "163805070008040065005007008450082039301000040700000000839050000604200590000093081"

#First put in rules for the values that are in the sudoku puzzle
row = 1
column = 1

for char in input:

    if char != "0":
        print("c entry (" + str(row) + "," + str(column) + ") contains a " + str(char))
        value = 81 * (int(row) - 1) + 9 * (int(column) - 1) + int(char) - 1 + 1
        print(str(value) + " 0")
    
    column += 1
 
    if column == 9:
        column = 1
        row += 1
        
