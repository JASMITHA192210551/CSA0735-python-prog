def nth_largest(nums, n):
    if n <= 0:
        return "Invalid input"
    elif n > len(nums):
        return "N is larger than the list length"
    else:
        nums.sort(reverse=True)
        return f"{n}th Largest number: {nums[n-1]}"

# Test cases:
print(nth_largest([14, 67, 48, 23, 5, 62], 4))
