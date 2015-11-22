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
# No. of clauses = 8829 (for 9x9 sudoku) + clauses for filled in cells
cnf_file.write("p cnf 729 " + str(clauses) + "\n")

# Write clauses for "Every cell contains at least one number"
cnf_file.write("c # Rules: \"Every cell contains at least one number\"\n")
for i in range(0, 9):
    for j in range(0, 9):
        cnf_file.write("c i:"+str(i)+" j:"+str(j)+"\n")
        for k in range(1, 10):
            cnf_file.write(str(81*i + 9*j + k) + " ")
        cnf_file.write("0\n")

# Write clauses for "Each number appears at most once in every row"
cnf_file.write("c # Rules: \"Each number appears at most once in every row\"\n")
for i in range(0, 9):
    for k in range(1, 10):
        for j in range(0, 8):
            for l in range(j + 1, 9):
                cnf_file.write("c i:"+str(i)+" k:"+str(k)+" j:"+str(j)+" l:"+str(l)+"\n")
                cnf_file.write(str(-(81*i + 9*j + k)) + " " + str(-(81*i + 9*l + k)) + " 0\n")

# Write clauses for "Each number appears at most once in every column"
cnf_file.write("c # Rules: \"Each number appears at most once in every column\"\n")
for j in range(0, 9):
    for k in range(1, 10):
        for i in range(0, 8):
            for l in range(i+1, 9):
                cnf_file.write("c j:"+str(j)+" k:"+str(k)+" i:"+str(i)+" l:"+str(l)+"\n")
                cnf_file.write(str(-(81*i + 9*j + k)) + " " + str(-(81*l + 9*j + k)) + " 0\n")


# Write clauses for "Each number appears at most one in every 3x3 sub-grid"
cnf_file.write("c # Rules: \"Each number appears at most one in every 3x3 sub-grid\"\n")
for k in range(1, 10):
    for a in range(0, 3):
        for b in range(0, 3):
            for u in range(0, 3):
                for v in range(0, 2):
                    for w in range(v + 1, 3):
                        cnf_file.write("c k:"+str(k)+" a:"+str(a)+" b:"+str(b)+" u:"+str(u)+" v:"+str(v)+" w:"+str(w)+"\n")
                        cnf_file.write(str(-(81*(3*a + u) + 9*(3*b + v) + k)) + " " + str(-(81*(3*a + u) + 9*(3*b + w) + k)) + " 0\n")

cnf_file.write("c <New set>\n")
for k in range(1, 10):
    for a in range(0, 3):
        for b in range(0, 3):
            for u in range(0, 2):
                for v in range(0, 3):
                    for w in range(u+1, 3):
                        for t in range(0, 3):
                            cnf_file.write("c k:"+str(k)+" a:"+str(a)+" b:"+str(b)+" u:"+str(u)+" v:"+str(v)+" w:"+str(w)+" t:"+str(t)+"\n")
                            cnf_file.write(str(-(81*(3*a + u) + 9*(3*b + v) + k)) + " " + str(-(81*(3*a + w) + 9*(3*b + t) + k)) + " 0\n")

cnf_file.write("c # Start of Puzzle\n")
#Add the clauses for the values that are in the sudoku puzzle
row = 1
column = 1

for char in input:

    if char != "0":
        value = 81 * (int(row) - 1) + 9 * (int(column) - 1) + int(char) - 1 + 1
        cnf_file.write(str(value) + " 0\n")

    column += 1

    if column == 10:
        column = 1
        row += 1

cnf_file.closed
