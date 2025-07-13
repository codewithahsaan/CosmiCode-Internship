# Recursive Fibonacci Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Fibonacci Function
def fibonacci_iterative(n):
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

# Main Execution
n = 30

print("First 30 Fibonacci numbers (Iterative):")
print(fibonacci_iterative(n))

print("\nFirst 30 Fibonacci numbers (Recursive):")
recursive_fib = [fibonacci_recursive(i) for i in range(n)]
print(recursive_fib)
