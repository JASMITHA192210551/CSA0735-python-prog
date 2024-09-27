def calculategrade(percentage):
    if(percentage>=75):
        return "distinction"
    elif(percentage>=60):
        return "first division"
    elif(percentage>=50):
        return "second division"
    elif(percentage>=40):
        return "third division"
    else:
        return "fail"
py=90
cprg=91
math=92
phy=93
total=py+cprg+phy+math
percentage=total//4
print("grade : ",calculategrade(percentage))
