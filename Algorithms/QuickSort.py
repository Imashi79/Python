#QuickSort algorythm implementation
def QuickSort(A, p , r):
    if p < r :
        q = PARTITION(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

def PARTITION(A,p,r):
    X= A[r]
    i = p-1
    for j in range(p,r-1):
        if A[j] <= X:
            i = i + 1
            A[i],A[j] = A[j], A[i]
    A[i+1] ,A[r] = A[r], A[i+1]
    return i+1
    

#Getting inputs
marks = []

for i in range (0,5):
    marks.append(int(input("Enter mark: ")))

print("\nInput marks")
print(marks)


QuickSort(marks,0,len(marks)-1)#call the sorting function

print("Sorted marks") #print sorted marks
print(marks)
