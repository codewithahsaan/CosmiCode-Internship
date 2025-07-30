def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target:
            return mid  # Found the target
        elif guess < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Target not found


sorted_numbers = [1, 3, 5, 7, 9, 11,12,18]
target_value = int(input("Enter the number to search: "))

result = binary_search(sorted_numbers, target_value)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found in the list.")
