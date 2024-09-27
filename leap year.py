date=4
month=11
year=1947
if year%4==0 or year%400==0 and year%100!=0:
    print(year," is leap")
else:
    print(year,"is not leap")
