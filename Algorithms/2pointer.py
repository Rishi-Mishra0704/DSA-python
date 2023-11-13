def two_pointer_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10

result = two_pointer_sum(sorted_array, target_sum)

if result:
    print(f"Pair found: {result[0]}, {result[1]}")
else:
    print("No pair found.")
