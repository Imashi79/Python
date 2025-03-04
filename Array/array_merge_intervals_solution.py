"""
Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
For example,
Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
return [[1, 10], [11, 18], [19, 22]]
"""

def merge_intervals(intervals):
    if not intervals:
        return []

    merged = [intervals[0]]  # Initialize with the first interval

    for i in range(1, len(intervals)):
        prev = merged[-1]  # Last interval in merged list
        curr = intervals[i]  # Current interval

        if prev[1] >= curr[0]:  # Overlapping condition
            prev[1] = max(prev[1], curr[1])  # Merge intervals
        else:
            merged.append(curr)  # No overlap, add the interval

    return merged

original_Intervals = [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]
merged_intervals = merge_intervals(original_Intervals)
print(merged_intervals)
