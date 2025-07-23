import string

def find_longest_word(sentence):
    # Remove punctuation using str.translate
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    words = cleaned_sentence.split()
    
    # Find the longest word
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

# User input
user_input = input("Enter a sentence: ")

# Find and show longest word
longest_word = find_longest_word(user_input)
print("The longest word is:", longest_word)
