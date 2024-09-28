def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point to divide the array into two halves
        mid = len(arr) // 2
        
        # Dividing the elements into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive call to merge_sort for both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Initialize variables for merging process
        i = j = k = 0
        
        # Merge the left and right halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any elements were left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check if any elements were left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
