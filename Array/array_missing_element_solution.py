# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number

def finder(arr1, arr2):
    num = sum(arr1) - sum(arr2)
    return (num)

first_arr = [1,2,3,4,5,6,7]
second_arr = [3,7,2,1,4,6]

print("First array : ", first_arr)
print("Second arrayy : ", second_arr)
print ("missing value : ", finder(first_arr,second_arr))

#find two missing values
def findvalues(arr1, arr2):
    nums = set(arr1) - set(arr2)
    return (nums)

first_arr = [1,2,3,4,5,6,7]
second_arr = [3,7,2,4,6]

print("First array : ", first_arr)
print("Second arrayy : ", second_arr)
print ("missing value : ", findvalues(first_arr,second_arr))
