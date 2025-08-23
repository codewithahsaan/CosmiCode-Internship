def complex_calculations(a, b):
    try:
        # Example operations
        result1 = a / b                    # Division (may cause ZeroDivisionError)
        result2 = (a ** b)                 # Exponentiation (may cause OverflowError)
        result3 = float(a) + float(b)      # Conversion (may cause ValueError)
        
        print("Division Result:", result1)
        print("Power Result:", result2)
        print("Addition Result:", result3)

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
    except ValueError:
        print("❌ Error: Invalid value entered, cannot convert to float!")
    except OverflowError:
        print("❌ Error: Number too large to handle!")
    except TypeError:
        print("❌ Error: Unsupported data types provided!")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    finally:
        print("✅ Calculation attempt finished.")

# --- Example Runs ---
print("Case 1: Normal inputs")
complex_calculations(10, 2)

print("\nCase 2: Division by zero")
complex_calculations(5, 0)

print("\nCase 3: Very large exponent")
complex_calculations(10, 1000000)

print("\nCase 4: Wrong type input")
complex_calculations("abc", 2)
