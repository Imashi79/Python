#implement bubble sort algorythm
def BUbbleSort(A):
    for i in range (0, len(A)-1):
        for j in range (0, len(A)-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1], A[j]


#Getting inputs
A = []

for i in range (0,5):
    A.append(int(input("Enter number: ")))

print("\nInput marks")
print(A)


BUbbleSort(A)#call the sorting function

print("Sorted marks") #print sorted marks
print(A)


