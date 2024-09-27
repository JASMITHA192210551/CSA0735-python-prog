def calculate(expression):
    result = 0
    sign = 1
    num = 0

    for char in expression:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in ['+', '-']:
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1

    result += sign * num
    return result

# Example usage:
print(calculate("2+3-1"))
