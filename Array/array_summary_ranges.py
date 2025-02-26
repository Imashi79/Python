"""
Given a sorted integer array without duplicates,
return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

def summary_ranges(arr):
    if not arr:
        return []
    
    result = []
    start = arr[0]

    for i in range(1,len(arr)):
       if arr[i-1]+ 1 != arr[i]:
            # If range length is more than 1, add the range
            if start == arr[i-1]:
                result.append(str(start))  # Single number range
            else:
                result.append(f"{start}->{arr[i-1]}")  # Range
            start = arr[i]  # Update start to the current number
    
    # Handle the last range or number
    if start == arr[-1]:
        result.append(str(start))  # Single number
    else:
        result.append(f"{start}->{arr[-1]}")  # Final range
    return result
    
arr = [0,1,2,4,5,7]
arr1 = [0,2,3,4,6,8,9]
print(summary_ranges(arr))
print(summary_ranges(arr1))


