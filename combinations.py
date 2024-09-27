def findcombination(number):
    digit=[int(d) for d in str(number)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i!=j and j!=k and k!=i:
                    print(digit[i],digit[j],digit[k])
number=int(input("enter number : "))
findcombination(number)
