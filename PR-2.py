def find_max_min(arr, low, high): 
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]  
        else:
            return arr[high], arr[low]  
    mid = (low + high) // 2
    min1, max1 = find_max_min(arr, low, mid)  
    min2, max2 = find_max_min(arr, mid + 1, high)  
    overall_min = min(min1, min2)
    overall_max = max(max1, max2)
    return overall_min, overall_max
# Example usage
arr = [3, 5, 1, 9, 2, 8, 4, 7]
n = len(arr)
min_val, max_val = find_max_min(arr, 0, n - 1)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")