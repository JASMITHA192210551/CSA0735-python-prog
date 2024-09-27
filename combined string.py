s1="welcome"
s2="homely"
s3=""
max_len=max(len(s1),len(s2))
for i in range(max_len):
    if i<len(s1):
        s3+=s1[i]
    if i<len(s2):
        s3+=s2[i]
vowels="aeiouAEIOU"
vc=0
for char in s3:
    if char in vowels:
        vc+=1
print("combined string =",s3)
print("vowel count :",vc)
    
