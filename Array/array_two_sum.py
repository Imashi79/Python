# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution

# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].

size = int(input("Enter Size of number series : "))

arr = []
result = []

# Getting the array input from the user
for i in range(size):
    num = int(input(f"Enter {i+1} element: "))
    arr.append(num)
           
target = int(input("Enter target number: "))

# Finding two numbers in the array that add up to the target
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            result.append(i)
            result.append(j)
            break

# Displaying the result
print(f"Given nums = {arr}, target = {target}")
if not result:
    print("Target not found.")
else:
    print(f"Because nums[{result[0]}] + nums[{result[1]}] = {arr[result[0]]} + {arr[result[1]]} = {target}")
    print(f"returns {result}")



### we can also use 'enumerate(arr)' build in fuction to forlopp, enumerate(arr) return both index and value same time