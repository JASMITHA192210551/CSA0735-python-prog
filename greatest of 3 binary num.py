bin1=input("enter bin1 value:")
bin2=input("enter bin2 value:")
bin3=input("enter bin3 value:")
a=int(bin1,2)
b=int(bin2,2)
c=int(bin3,2)
if a>b and a>c:
    print("greatest is : ",bin(a)[2:])
elif b>a and b>c:
    print("greatest is : ",bin(b)[2:])
else:
    print("greatest is : ",bin(c)[2:])
