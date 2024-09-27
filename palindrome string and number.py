 choice=input("choice(s or n) :")
if choice.lower()=='s':
    input="madam"
    rev_str=""
    for i in range(len(input)-1,-1,-1):
        rev_str+=input[i]
    if input==rev_str:
        print("string palindrome")
    else:
        print("not a string palindrome")
        
elif choice.lower()=='n':
    n=121
    rev=0
    k=n
    while n>0:
        d=n%10;
        rev=rev*10+d
        n//=10
if(rev==k):
    print("number palindrome")
else:
    print("not a number palindrome")
