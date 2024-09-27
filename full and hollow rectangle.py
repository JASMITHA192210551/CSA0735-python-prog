choice=input("enter choice (f/h) : ")
if choice=='f':
    m=4
    n=7
    for i in range(m):
        for j in range(n):
            print("$",end=" ")
        print()
elif choice=='h':
    m=4
    n=7
    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                print("$",end=" ")
            else:
                 print(" ",end=" ")
        print()
