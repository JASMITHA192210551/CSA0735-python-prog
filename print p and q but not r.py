def calculate(p,q,r):
    for num in range(p,q+1):
        if str(r) not in str(num):
            print(num,end=" ")
p=60
q=70
r=3
print("numbers are : ",end=" ")
calculate(p,q,r)
            
