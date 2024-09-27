n=153
sum=0
k=n
while n!=0:
    d=n%10
    sum=sum+d*d*d
    n//=10
if k==sum:
    print("asn")
else:
    print("not asn")
