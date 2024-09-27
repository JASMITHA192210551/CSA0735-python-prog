bin_num=input("enter number")
choice=input("conversion(D/O)")
if choice.upper()=='D':
    dec_num=int(bin_num,2)
    print("decimal num : ",dec_num)
elif choice.upper()=='O':
   dec_num=int(bin_num,2)
   oct_num=format(dec_num,'o')
   print("octal num:",oct_num)
