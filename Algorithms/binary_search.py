def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            print(f"Target found at index {mid}")
            return mid  # Target found, return the index
        elif mid_value > target:
            high = mid - 1  # Search in the left half
        else:
            low = mid + 1   # Search in the right half

    return -1  # Target not found


# Driver code
arr = [1, 2, 3, 4, 5]
target = 4
result = binary_search(arr, target)