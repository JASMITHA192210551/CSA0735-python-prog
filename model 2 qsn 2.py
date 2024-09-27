n=8
n1=0
n2=1
y=[]
for i in range(n):
    y.append(n1)
    next=n1+n2
    n1=n2
    n2=next
print(y)
print("nth fibonacci : ",y[n-1])
