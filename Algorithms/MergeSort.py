#MergeSort algorithm implementation
def MergeSort(A, p , r):
    if p < r :
        q = (p+r)//2
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)

def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    
    for i in range (n1):
        L[i] = A[p+i]
    
    for j in range (n2):
        R[j] = A [q+j+1]
    
    L[n1] = float('inf')
    R[n2] = float('inf') 
    
    i = 0
    j = 0
    
    for k in range (p , r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    

#Getting inputs
marks = []

for i in range (0,5):
    marks.append(int(input("Enter mark: ")))

print("\nInput marks")
print(marks)


MergeSort(marks,0,len(marks)-1)#call the sorting function

print("Sorted marks") #print sorted marks
print(marks)

