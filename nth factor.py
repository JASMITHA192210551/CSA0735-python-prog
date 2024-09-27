n=100
y=[]
for i in range(1,n+1):
    if n%i==0:
        y.append(i)
        m=4
print(y,end=" ")
print()
print(m,"th factor :",y[m-1])
