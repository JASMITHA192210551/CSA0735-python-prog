def find_nth_largest(numbers, n):
    numbers = sorted(numbers, reverse=True)
    return numbers[n-1]
numbers = [14, 67, 48, 23, 5, 62]
n = 4
result = find_nth_largest(numbers, n)
print(f"{n}th Largest number: {result}")
