l=1
u=40
ps=[]
for i in range(l,u+1):
    root=int(i**0.5)
    if root*root==i:
        sum=0
        n=i
        while n>0:
            sum+=n%10
            n//=10
        if sum<10:
            ps.append(i)
print(ps)
