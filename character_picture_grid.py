
#Program will transpose the matrix named 'grid' and print it out

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0 #9 rows
y = 0 #6 columns

while y <= 5:               #Increments both x and y indices
    while x <= 8:           #Increments x index, but not the y index. Moves down column [0] and prints items
        print (grid[x][y], end="")
        x += 1
    print ('\n')            #Prints new line after each column has been completed
    x = 0                   #Reset x to 0
    print (grid[x][y], end="")
    x += 1
    y += 1


