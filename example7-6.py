# EXAMPLE 7.6. The matrix T represents a table of high jump records (first jump), where the rows represent the athlete's name
# and the columns represent the different heights jumped by the athlete. The symbols stored in the table are: x, 
# valid jump; 0, null or unattempted jump.

#mxn = rowxcolumn
amountOfRows = 3
amountOfColumns = 5
matrix = []

for row in range(amountOfRows):
    matrix.append(['hola'])
    for column in range(amountOfColumns):
        matrix[row].append([])

for row in matrix:
    for value in row:
        print("\t", value, end=" ")
    print()
