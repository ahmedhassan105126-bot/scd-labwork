import time

seconds = int(input("How many seconds to count down? "))

for i in range(seconds, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("Time's up! 🚀")
