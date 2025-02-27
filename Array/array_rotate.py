''' Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem. '''


arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 3
result = []
result1 = arr[:]


for i in range(k+1,n):
    result.append(arr[i])

for i in range(k+1):
    result.append(arr[i])

print("array : " , arr)
print("rotated array : ",result)


for i, x in enumerate(arr):
    if i + k < n :
        result1[i + k] = arr[i]

    else :
        result1[(i + k) - n] = arr[i]

print()
print("array : " , arr)
print("rotated array : ",result1)




