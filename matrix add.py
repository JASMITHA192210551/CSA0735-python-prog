matrix1=[[1,2],[5,3]]
matrix2=[[2,3],[4,1]]
result=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
print("resultant matrix : ")
for row in result:
    print(row)
        
