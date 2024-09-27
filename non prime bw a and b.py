a=int(input("enter a value : "))
b=int(input("enter b value : "))
for i in range(a+1,b):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(i)
                break
