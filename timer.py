import time

while True:
    my_time = input("Enter time in seconds: ")
    if my_time.isdigit() and int(my_time) > 0:
        break
    print("Invalid input. Please enter a positive integer.")

my_time = int(my_time)

for x in reversed(range(my_time + 1)):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME IS UP!")
