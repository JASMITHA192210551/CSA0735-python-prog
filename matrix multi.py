A = [[2, 1], [3, 4]]
B = [[31, 1], [1, 2]]
if len(A[0]) != len(B):
    print("Matrices cannot be multiplied")
else:
    C = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    print("Matrix A:")
    for row in A:
        print(row)
    print("Matrix B:")
    for row in B:
        print(row)
    print("Matrix C (A * B):")
    for row in C:
        print(row)
