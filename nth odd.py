def nth_odd_after_n(n):
    nth_odd=2*(n)-1
    nth_odd_after=2*(nth_odd)+1
    return nth_odd_after
n=int(input("enter input:"))
print(f"{n}th odd number after {n} odd num={nth_odd_after_n(n)}")
