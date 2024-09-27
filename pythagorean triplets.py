limit=int(input("enter limit :"))
for a in range(1,limit+1):
    for b in range(a,limit):
        c=(a*a+b*b)**0.5
        if (c==int(c) and c<=limit):
            print(a,b,int(c))
