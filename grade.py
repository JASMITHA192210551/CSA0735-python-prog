def calculategrade(percentage):
    if(percentage>=90):
        return 'S'
    elif(percentage>=80):
        return 'A'
    elif(percentage>=70):
        return 'B'
    elif(percentage>=60):
        return 'C'
    elif(percentage>=50):
        return 'D'
    else:
        return 'fail'
percentage=float(input("enter marks :"))
print("grade : ",calculategrade(percentage))
