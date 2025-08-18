class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    # Write to a file (overwrites if file already exists)
    def write_file(self, content):
        with open(self.filename, "w") as file:
            file.write(content)
        print(f"✅ Content written to {self.filename}")

    # Append content to a file
    def append_file(self, content):
        with open(self.filename, "a") as file:
            file.write(content)
        print(f"➕ Content appended to {self.filename}")

    # Read content from a file
    def read_file(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
            print(f"📖 Reading {self.filename}:")
            return content
        except FileNotFoundError:
            print("⚠️ File not found!")
            return ""


# ✅ Example usage
file_handler = FileHandler("example.txt")

# Writing to file
file_handler.write_file("Hello, this is the first line.\n")

# Appending to file
file_handler.append_file("This line is added later.\n")

# Reading file content
content = file_handler.read_file()
print(content)
