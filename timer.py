import time
from datetime import timedelta

while True:
    try:
        my_time = int(input("Enter time in seconds: "))
        if my_time > 0:
            break
        else:
            print("Invalid input. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

time_delta = timedelta(seconds=my_time)

for delta in reversed(range(my_time)):
    time_left = str(time_delta - timedelta(seconds=delta))
    print(time_left[-8:])
    time.sleep(1)

print("TIME IS UP!")
