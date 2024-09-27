decimal=12
binary=""
while decimal>0:
    rem=decimal%2
    binary=str(rem)+binary
    decimal//=2
print("binary values :",binary)
