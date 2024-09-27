a=[1,2,2,3,3,3,4,4,4,4]
freq={}
for num in a:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)
