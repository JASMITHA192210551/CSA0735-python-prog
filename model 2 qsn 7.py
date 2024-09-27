date=4
month=11
year=1947
if year%4==0 or year%400==0 and year%100!=0:
    print("leap year and next leap year is ",year+4)
else:
    print("not a leap year and previous leap year is ",date,"/",month,"/",year-1)
    
