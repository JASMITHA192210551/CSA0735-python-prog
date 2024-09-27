string="TEMPLE"
repeated=[]
for letter in string:
    if string.count(letter)>1 and letter not in repeated:
        repeated+=letter
print("repeated letters : ",len(repeated))
print("repeted string : ",repeated)
