def movezeros(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j]=nums[i]
            j+=1
    for j in range(i,len(nums)):
        nums[i]=0
nums=[1,0,12,15,0,0,4]
movezeros(nums)
print(nums)
