a=[14,16,87,36,25,89,34]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
m=1
n=3
max=a[len(a)-m]
min=a[n-1]
print("mth max : ",max)
print("nth min : ",min)
print("sum is : ",max+min)
print("diff is : ",max-min)
