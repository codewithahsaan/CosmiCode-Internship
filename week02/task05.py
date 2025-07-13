def max_subarray_kadane(arr):
    max_current = max_global = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            s = i
        else:
            max_current += arr[i]

        if max_current > max_global:
            max_global = max_current
            start = s
            end = i

    return max_global, arr[start:end+1]

# Main Execution
arr = list(map(int, input("Enter list of numbers (space-separated): ").split()))

max_sum, subarray = max_subarray_kadane(arr)

print(f"Maximum subarray sum is: {max_sum}")
print(f"Subarray with maximum sum is: {subarray}")
