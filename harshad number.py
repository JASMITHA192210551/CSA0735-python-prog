n=21
sum=0
k=n
while n!=0:
    sum+=n%10
    n//=10
if(k%sum==0):
    print("harshad number")
else:
    print("not harshad number")
