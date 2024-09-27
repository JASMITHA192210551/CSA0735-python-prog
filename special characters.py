str="Modi Birthday @September 17,#$&%"
v=""
c=""
d=""
s=""
vowels="aeiouAEIOU"
vc=cc=dc=sp=sc=0
for char in str:
    if char.isalpha():
        if char in vowels:
            v+=char
            vc+=1
        else:
            c+=char
            cc+=1
    elif char.isdigit():
        d+=char
        dc+=1
    elif char==" ":
        sp+=1
    else:
        s+=char
        sc+=1
print("vowels : ",v)
print("vc :",vc)
print("consonants :",c)
print("cc: ",cc)
print("digits : ",d)
print("dc : ",dc)
print("sp :",sp)
print("special char:",s)
print("sc: ",sc)
