def matrix_multiply(A, B):
    # Check if multiplication is possible (columns of A == rows of B)
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible: Incompatible dimensions.")
        return None

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform multiplication
    for i in range(len(A)):  # rows of A
        for j in range(len(B[0])):  # columns of B
            for k in range(len(B)):  # shared dimension
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example matrices
A = [
    [1, 2],
    [3, 4],
    [5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

# Multiply matrices
product = matrix_multiply(A, B)

# Display result
if product:
    print("Result of Matrix Multiplication:")
    for row in product:
        print(row)
