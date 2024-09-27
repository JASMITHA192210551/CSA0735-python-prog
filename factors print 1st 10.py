n=100
y=[]
for i in range(1,n+1):
    if n%i==0:
        y.append(i)
print(y,end=" ")
print()
print("total no of factors:",len(y))
m=int(input("enter m value:"))
for j in range(m):
    print(y[j],end=" ")
