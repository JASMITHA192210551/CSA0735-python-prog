n=3
a=121
for i in range(n):
    for j in range(i+1):
        print(a,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(a,end=" ")
    print()
