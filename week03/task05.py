import string

def most_frequent_word(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        # Remove punctuation and convert to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        
        # Split into words
        words = text.split()
        
        # Count word frequencies
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # Find the most frequent word
        most_frequent = max(word_count, key=word_count.get)
        frequency = word_count[most_frequent]

        print("Most frequent word:", most_frequent)
        print("Frequency:", frequency)
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Example usage
filename = input("Enter the path to the text file: ")
most_frequent_word(filename)
