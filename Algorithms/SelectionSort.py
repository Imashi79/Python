#selection Sort implementation
def SelectSort(A):
    for i in range (0, len(A)-1):
        key = i
        for j in range (i+1 , len(A)):
            if A[j] < A[key]:
                key = j
        A[i],A[key] = A[key],A[i]

#Getting inputs
marks = []

for i in range (0,5):
    marks.append(int(input("Enter mark: ")))

print("\nInput marks")
print(marks)


SelectSort(marks)#call the sorting function

print("Sorted marks") #print sorted marks
print(marks)

