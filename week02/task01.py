def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def list_primes_upto(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

# Main program
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# all prime numbers up to the number
print(f"Prime numbers up to {number}:")
print(list_primes_upto(number))
