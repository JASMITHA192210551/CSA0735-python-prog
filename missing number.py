def missingnum(nums):
    n=len(nums)
    e_s=n*(n+1)//2
    a_s=sum(nums)
    return e_s-a_s
nums=[3,0,1]
print("missing num : ",missingnum(nums))
