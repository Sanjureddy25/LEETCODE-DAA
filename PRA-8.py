def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
# Example input:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Calling the function:
merged_intervals = merge_intervals(intervals)

# Output:
print(merged_intervals)  # Output: [[1, 6], [8, 10], [15, 18]]
