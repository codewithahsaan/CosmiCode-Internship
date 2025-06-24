def power(base, exponent):
    """Returns base raised to the power of exponent."""
    return base ** exponent

def modulo(a, b):
    """Returns the remainder when a is divided by b."""
    if b == 0:
        return "Error: Division by zero."
    return a % b

def main():
    print("Advanced Arithmetic Operations")
    print("1. Power (a^b)")
    print("2. Modulo (a % b)")

    choice = input("Choose operation (1 or 2): ")

    if choice == '1':
        a = float(input("Enter base (a): "))
        b = float(input("Enter exponent (b): "))
        result = power(a, b)
        print(f"{a} ^ {b} = {result}")

    elif choice == '2':
        a = int(input("Enter dividend (a): "))
        b = int(input("Enter divisor (b): "))
        result = modulo(a, b)
        print(f"{a} % {b} = {result}")

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
