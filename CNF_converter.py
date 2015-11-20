# Open the file to write the output
cnf_file = open("sudoku.cnf", 'w')

clauses = 8829

#Test input
input = "163805070008040065005007008450082039301000040700000000839050000604200590000093081"

#Find the no. of filled in cells
for char in input:
    if char != "0":
	clauses += 1
        

# DIMACS Structure:
# Every commented line begins with a lowercase c
# The first line of the problem starts with a lowercase p, problem type (cnf), # of variables, and # of clauses
# The following lines define each clause, and must end with a 0



# Let N be the no. of distinct symbols
# No. of variables = N^3. In normal cases, we have 9 distinct symbols. 9^3 = 729
# No. of clauses = N^2 + l3Y58T7GFT
cnf_file.write("p cnf 729 " + str(clauses) + "\n")

# Write clauses for "Every cell contains at least one number"
for h in range(0, 9):
	for i in range(0, 9):
		for j in range(1, 10):
			cnf_file.write(str(81*h + 9*i + j) + " ")
        	cnf_file.write("0\n")

# Write clauses for "Each number appears at most once in every row"


# Write clauses for "Each number appears at most once in every column"


# Write clauses for "Each number appears at most one in every 3x3 sub-grid"


#Add the clauses for the values that are in the sudoku puzzle
row = 1
column = 1

for char in input:

    if char != "0":
        cnf_file.write("c entry (" + str(row) + "," + str(column) + ") contains a " + str(char) + '\n') #Remove this line later?
        value = 81 * (int(row) - 1) + 9 * (int(column) - 1) + int(char) - 1 + 1
        cnf_file.write(str(value) + " 0\n")
    
    column += 1
 
    if column == 10:
        column = 1
        row += 1

cnf_file.closed
