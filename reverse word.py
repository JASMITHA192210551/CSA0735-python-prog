word=input("enter word: ")
rev_word=""
for i in range(len(word)-1,-1,-1):
    rev_word+=word[i]
print("reverse word is :",rev_word)
