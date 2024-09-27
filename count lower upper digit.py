def count():
    uc=lc=dc=0
    while True:
        char=input("enter any character : ")
        if char=='*':
            break
        elif char.isupper():
            uc+=1
        elif char.islower():
            lc+=1
        elif char.isdigit():
            dc+=1
    print("upper count : ",uc)
    print("lower count : ",lc)
    print("digit count : ",dc)
count()
