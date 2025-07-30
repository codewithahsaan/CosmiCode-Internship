def count_char_frequency(text):
    frequency = {}

    for char in text:
        if char != ' ':  # Skip spaces
            char = char.lower()  # Make it case-insensitive
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency

# Get input from user
user_input = input("Enter a string: ")

# Count frequency
char_counts = count_char_frequency(user_input)

# Display results
print("\nCharacter Frequencies:")
for char, count in char_counts.items():
    print(f"'{char}': {count}")
