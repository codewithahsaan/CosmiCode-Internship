def find_largest(a, b, c):
    """Returns the largest."""
    return max(a, b, c)

def find_smallest(a, b, c):
    """Returns the smallest."""
    return min(a, b, c)

def main():
    print("Enter three numbers to find the largest and smallest:")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")

    largest = find_largest(num1, num2, num3)
    smallest = find_smallest(num1, num2, num3)

    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")

if __name__ == "__main__":
    main()
