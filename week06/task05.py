import threading
import time

# Task 1: Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"🔢 Number: {i}")
        time.sleep(1)

# Task 2: Print letters
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"🔤 Letter: {letter}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("✅ Both threads finished execution!")
