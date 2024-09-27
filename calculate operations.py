def operation(x,n,choice):
    print("1.power :")
    print("2.addition :")
    print("3.subtraction :")
    print("4.multiplication")
    print("5.division:")
    if choice==1:
        return pow(x,n)
    elif choice==2:
        return x+n
    elif choice==3:
        return x-n
    elif choice==4:
        return x*n
    elif choice==5:
        if n!=0:
            return x//n
        else:
            "division not allowed "
    else:
        return "invalid choice"
choice=int(input("enter choice (1/2/3/4/5) : "))
x=4
n=2
result=operation(x,n,choice)
print("result : ",result)
