def rotateMatrix(mat):
    for i in range(len(mat)):
        for j in range(i):

            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    for i in range(len(mat)):
        for j in range(len(mat)//2):

            mat[i][j],mat[i][-1] = mat[i][-1] ,mat[i][j]
    
    
    for x in mat:
        for j in x:
            print(j,end="|")
        print()
    


mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]


rotateMatrix(mat)