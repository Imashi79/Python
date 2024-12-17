#InsertSort Algorythm implementation
def InsertSort(A):
    for j in range (1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

#gettin input
A = []
for i in range (1,5):
    A.append(int(input("Enter integer number : ")))

#print input values
print("\nInput values")
print(A)

InsertSort(A)

#print sorted values
print("\nSorted values")
print(A)