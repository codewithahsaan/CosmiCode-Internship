import time

# Decorator function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()   # record start
        result = func(*args, **kwargs)  # run the function
        end_time = time.time()     # record end
        execution_time = end_time - start_time
        print(f"⏱️ Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper

# Example function 1
@measure_time
def slow_function():
    time.sleep(2)  # simulating a slow process
    print("Slow function finished.")

# Example function 2
@measure_time
def fast_function(n):
    total = sum(range(n))
    return total

# Run the functions
slow_function()
print("Result of fast_function:", fast_function(1000000))
