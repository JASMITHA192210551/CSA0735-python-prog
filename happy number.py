def is_happy_number(n):
    while n != 1 and n != 4:
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

num = int(input("Enter number: "))
if is_happy_number(num):
    print("Given number is a happy number")
else:
    print("Given number is not a happy number")
