def prime_factors(n):
    factors = []
    # Factor out 2s first
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check odd numbers starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors

# Main Execution
num = int(input("Enter a number: "))
print(f"Prime factors of {num} are: {prime_factors(num)}")
