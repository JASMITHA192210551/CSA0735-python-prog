n1=16
n2=20
gcd=min(n1,n2)
while n1%gcd!=0 or n2%gcd!=0:
    gcd-=1
lcm=n1*n2//gcd
print("gcd is : ",gcd)
print("lcm is : ",lcm)
