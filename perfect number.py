n=int(input("enter number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print(n,"is perfect")
else:
    print(n,"is not perfect")
