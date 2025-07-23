def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(text.lower().split())
    
    # Check if cleaned string is same as its reverse
    return cleaned == cleaned[::-1]

# User input
user_input = input("Enter a string: ")

# Check and print result
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
