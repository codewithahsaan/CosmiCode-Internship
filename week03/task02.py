def reverse_list(original_list):
    reversed_list = []
    for i in range(len(original_list) - 1, -1, -1):
        reversed_list.append(original_list[i])
    return reversed_list

# Example list
my_list = [10, 20, 30, 40, 50]

# Reverse it
reversed_result = reverse_list(my_list)

# Output
print("Original List:", my_list)
print("Reversed List:", reversed_result)
