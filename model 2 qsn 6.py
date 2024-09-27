a=12
b=19
c=""
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            print(i,end=" ")
            break
