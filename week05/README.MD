# 📘 Week 05 README: Object-Oriented Programming (OOP) Tasks

This repository contains seven Python programs demonstrating **core Object-Oriented Programming (OOP) principles** including **encapsulation, inheritance, polymorphism, and operator overloading**. Each task explores a different real-world problem modeled using OOP concepts.

---

### 🏦 1. Bank Account Class

**📝 Description:**
Defines a `BankAccount` class with attributes for **account number, balance, and owner name**. Provides methods for depositing, withdrawing, and transferring money.

**🧠 Concept Used:**

- Encapsulation (data and methods bundled in a class)
- Method definitions

**✅ What You Learn:**

- Managing object state (balance updates)
- Implementing transactions (deposit, withdraw, transfer)
- Simple class design for real-world systems

**🛠️ How We Solved This:**
We created methods `deposit()`, `withdraw()`, and `transfer()` to update balances safely, while preventing invalid transactions like overdrafts.

**📸 Screenshot:** `screenshots/bank_account.png`

---

### 🔺 2. Geometric Shapes (Circle, Rectangle, Triangle)

**📝 Description:**
Implements a **class hierarchy** for geometric shapes with methods to calculate **area and perimeter**.

**🧠 Concept Used:**

- Inheritance (Base class `Shape` → Derived classes `Circle`, `Rectangle`, `Triangle`)
- Method overriding

**✅ What You Learn:**

- Using inheritance to avoid code duplication
- Implementing shape-specific formulas for area and perimeter
- Polymorphic behavior when calling methods on derived objects

**🛠️ How We Solved This:**
Defined a base class `Shape` and derived classes with overridden methods: `area()` and `perimeter()`, implementing formulas specific to each shape.

**📸 Screenshot:** `screenshots/shapes.png`

---

### 🚗 3. Inheritance Example (Vehicle → Car, Bike)

**📝 Description:**
Demonstrates **inheritance** by creating a base class `Vehicle` and derived classes `Car` and `Bike`, each with unique features.

**🧠 Concept Used:**

- Inheritance (sharing attributes and methods)
- Method extension in subclasses

**✅ What You Learn:**

- How subclasses reuse base class functionality
- How subclasses can extend or specialize base class behavior

**🛠️ How We Solved This:**
We defined `Vehicle` with common attributes (e.g., brand, model), then extended it in `Car` and `Bike` classes with their own features.

**📸 Screenshot:** `screenshots/inheritance.png`

---

### ➕ 4. Operator Overloading (Complex Numbers)

**📝 Description:**
Implements **operator overloading** for a `ComplexNumber` class to perform arithmetic operations like addition and subtraction.

**🧠 Concept Used:**

- Operator overloading using `__add__`, `__sub__`, `__str__`
- Encapsulation of real and imaginary parts

**✅ What You Learn:**

- How Python allows custom behavior for operators
- How classes can mimic built-in data types

**🛠️ How We Solved This:**
We defined a `ComplexNumber` class with overloaded operators for arithmetic and a `__str__` method for user-friendly printing.

**📸 Screenshot:** `screenshots/complex_numbers.png`

---

### 🔄 5. Polymorphism Example

**📝 Description:**
Shows **polymorphism** by defining a base class with a method and overriding it in multiple derived classes.

**🧠 Concept Used:**

- Polymorphism (same method name, different behavior)
- Method overriding

**✅ What You Learn:**

- How polymorphism enables flexibility in OOP
- How the same interface can lead to different outcomes

**🛠️ How We Solved This:**
We created a base class with a method `speak()`, then derived classes (`Dog`, `Cat`) overrode it to provide unique outputs.

**📸 Screenshot:** `screenshots/polymorphism.png`

---

### 📚 6. Library Management System

**📝 Description:**
Implements a **Library System** with methods to **add, remove, and display books**.

**🧠 Concept Used:**

- Encapsulation (managing a collection of books in a class)
- List operations

**✅ What You Learn:**

- Managing collections of objects
- Building simple management systems using OOP

**🛠️ How We Solved This:**
We created a `Library` class that stored books in a list and methods `add_book()`, `remove_book()`, and `display_books()`.

**📸 Screenshot:** `screenshots/library.png`

---

### 📂 7. File Handling Class

**📝 Description:**
Implements a class for **basic file operations** like reading, writing, and appending to text files.

**🧠 Concept Used:**

- File handling with OOP
- Encapsulation of file operations

**✅ What You Learn:**

- Using Python’s file handling methods in a class
- Writing reusable file management utilities

**🛠️ How We Solved This:**
We created a `FileManager` class with methods `read_file()`, `write_file()`, and `append_file()` to handle text files efficiently.

**📸 Screenshot:** `screenshots/file_handling.png`

---

## 📌 Summary of Techniques Used

| Task             | Concept/Principle         | Key Features                    |
| ---------------- | ------------------------- | ------------------------------- |
| Bank Account     | Encapsulation             | Methods for transactions        |
| Geometric Shapes | Inheritance, Polymorphism | Area & Perimeter calculation    |
| Vehicle Example  | Inheritance               | Code reuse in subclasses        |
| Complex Numbers  | Operator Overloading      | `__add__`, `__sub__`, `__str__` |
| Polymorphism     | Method Overriding         | Same method, different behavior |
| Library System   | Encapsulation             | Managing a collection           |
| File Handling    | Encapsulation             | Read/Write/Append methods       |

---

## 📸 Screenshots (To Be Added)

- `screenshots/task01_code(1).png`
- `screenshots/task01_code(2).png`
- `screenshots/task01_output.png`
- `screenshots/task02_code(1).png`
- `screenshots/task02_code(2).png`
- `screenshots/task02_output.png`
- `screenshots/task03_code(1).png`
- `screenshots/task03_code(2).png`
- `screenshots/task03_output.png`
- `screenshots/task04_code.png`
- `screenshots/task04_output.png`
- `screenshots/task05_code(1).png`
- `screenshots/task05_code(2).png`
- `screenshots/task05_output.png`
- `screenshots/task06_code(1).png`
- `screenshots/task06_code(2).png`
- `screenshots/task06_output.png`
- `screenshots/task07_code.png`
- `screenshots/task07_output(1).png`
- `screenshots/task07_output(2).png`

(Add screenshots of your output in the `screenshots/` folder)

---

## 🧑‍💻 Author

**Muhammad Ahsaan**
CosmiCode Internship – Week 05 Tasks
[GitHub Repo Link](https://github.com/codewithahsaan/CosmiCode-Internship)
