def setZeroMatrix(mat):
    row_mat_len = len(mat)
    col_mat_len = len(mat[0])
    
    indexarr_row = [False]*row_mat_len
    indexarr_col = [False]*col_mat_len
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if (mat[x][y] == 0):
                indexarr_row[x] = True
                indexarr_col[y] = True

    for x in range(row_mat_len):
        
        for y in range(col_mat_len):
            if(indexarr_row[x]):
                mat[x] = [0]*col_mat_len    
            if(indexarr_col[y]):
                mat[x][y] = 0
            
    
    
    return mat          



def printMat(mat):
    for x in mat:
        for j in x:
            print(j,end=" | ")
        print(" ")
    


mat = [
        [1,2,0,5],
        [4,5,6,7],
        [7,0,9,9],
        [10,11,12,7]
        ]

print(printMat(mat))
print(printMat(setZeroMatrix(mat)))
