from datetime import datetime

def find_day(day, month, year):
    date = datetime(year, month, day)
    return date.strftime("%A")

# Example usage:
day = 31
month = 8
year = 2019
print(find_day(day, month, year)) 
