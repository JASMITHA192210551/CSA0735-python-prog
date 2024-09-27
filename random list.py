import random
a=20
b=50
n=5
list=[]
for _ in range(n):
    random_num=random.randint(a,b)
    list.append(random_num)
print(list)
