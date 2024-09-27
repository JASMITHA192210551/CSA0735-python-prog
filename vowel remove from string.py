string="we can play the game"
vowels="aeiouAEIOU"
vs=""
for char in string:
    if char not in vowels:
        vs+=char
print(vs)
        
