
from datetime import datetime

now = datetime.now()

print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current date: ", now.strftime("%Y-%m-%d"))
print("Current time: ", now.strftime("%H:%M:%S"))
