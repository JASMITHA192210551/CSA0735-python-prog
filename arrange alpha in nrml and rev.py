def alpha(word):
    word=word.lower()
    n_o=''.join(sorted(word))
    r_o=''.join(sorted(word,reverse=True))
    return n_o,r_o
word=input("enter charcter : ")
n_o,r_o=alpha(word)

print("normal order : ",n_o)
print("alpha order : ",r_o)



