# the size of row, column will be inputted
# next, put '*' or '.' randomly (can not exceed the size of row and column)
# '*' represent mine, and '.' represent safe zone
# for every '.' , print the number of adjacent mines (must include diagonal directions)


#   3 3     3 x 3 map

#   input of mines and safe zones
#   .**     two mines in the first row
#   *..     one mine in the second row
#   .*.     one mine in the third row

#   prints the number of adjacent mines in safe zones
#   2**
#   *43
#   2*1


col, row = map(int, input().split())

matrix = [] #initial blank map
for i in range(row):
    matrix.append(list(input()))    #filling up mines and safe zones

for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '.':     #if safe zone
            for a in range(i-1,i+2):    #checking adjacents
                for b in range(j-1, j+2):
                    if not(a<0 or b<0 or a>=row or b>=col):#prevented searching outside of the map
                        if matrix[a][b] == '*': #if mine is detected
                            count += 1
            matrix[i][j] = count    #replace '.' to the number of adjacent mines
            print(matrix[i][j], end='')
        else:   #if not safe zone, keep '*'
            print(matrix[i][j], end='')
    print()