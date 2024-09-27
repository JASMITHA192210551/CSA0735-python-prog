num=3025
sum=0
k=num
while num>0:
    d=num%100
    sum+=d**2
    num//=100
if sum==k:
    print("tech number ")
else:
    print("not tech number")
