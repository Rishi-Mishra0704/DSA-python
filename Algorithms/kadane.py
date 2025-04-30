def kadane(arr):
    current_max = max_sum = arr[0]

    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max+arr[i])
        max_sum = max(max_sum,current_max)

    return max_sum

# Example usage
if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print("Maximum contiguous sum is", kadane(arr))
    # Output: Maximum contiguous sum is 6