class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book.title}' added successfully!")

    # Remove a book by ID
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"❌ Book '{book.title}' removed successfully!")
                return
        print("⚠️ Book not found!")

    # Display all books
    def display_books(self):
        if not self.books:
            print("📚 No books available in the library.")
        else:
            print("\n📚 Library Books:")
            for book in self.books:
                print(book)


# ✅ Example usage
library = Library()

# Adding books
library.add_book(Book(1, "The Alchemist", "Paulo Coelho"))
library.add_book(Book(2, "1984", "George Orwell"))
library.add_book(Book(3, "Python Programming", "John Zelle"))

# Displaying all books
library.display_books()

# Removing a book
library.remove_book(2)

# Displaying again after removal
library.display_books()
