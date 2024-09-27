def count_chars():
    u = l = n = 0
    while (c := input("Enter any character: ")) != '*':
        u += c.isupper()
        l += c.islower()
        n += c.isdigit()
    print(f"Total count of lower case: {l}")
    print(f"Total count of upper case: {u}")
    print(f"Total count of numbers = {n}")

count_chars()
