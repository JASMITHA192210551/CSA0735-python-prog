def si(p,n,sc,g):
    if sc=='yes' and g=='f':
        rate=15
    elif sc=='yes' and g=='m':
        rate=12
    else:
        rate=10
    return (p*n*rate)/100
p=int(input("enter principle amount:"))
n=int(input("enter no of years :"))
sc=input("senior citizen (y/n)")
g=input("male/female")
print("simple interest :",si(p,n,sc,g))
