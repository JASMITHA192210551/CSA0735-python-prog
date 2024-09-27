names=input("enter names : ").split()
order=input("enter order (A/D):")
if order.upper()=='A':
    names.sort()
    print("sorted names in ao",names)
elif order.upper()=='D':
        names.sort(reverse=True)
        print("sorted names in do : ",names)
else:
        print("invalid input")
