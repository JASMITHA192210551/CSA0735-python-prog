string='''The apple doesn't fall. ...
All that glitters are not gold. ...
A picture is worth a thousand words. ...
Beggers can't be choosers. ...
A bird in the hand. ...
Better safe than sorry. ...
An apple a day keeps doctor away. ...
Blood is thicker than water. ...'''

str=string.split(". ...")
print("no of lines : ",len(str))

count=0
for i in str:
    words=i.split()
    for j in words:
        if j[0]=='B':
             count+=1
print("no of sentences that start with B : ",count)
