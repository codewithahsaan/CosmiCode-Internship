# Function to calculate GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Main Execution
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")
print(f"LCM of {num1} and {num2} is: {lcm(num1, num2)}")
