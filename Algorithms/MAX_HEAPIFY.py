def LEFT(i):
    return 2 * i + 1

def RIGHT(i):
    return 2 * i + 2

def MAX_HEAPIFY(A, i):
    l = LEFT(i)
    r = RIGHT(i)
    largest = i

    # Check if the left child exists and is greater than the current largest
    if l < len(A) and A[l] > A[largest]:
        largest = l

    # Check if the right child exists and is greater than the current largest
    if r < len(A) and A[r] > A[largest]:
        largest = r

    # Swap if the largest is not the current node and recurse
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A, largest)

# Example usage
A = [7, 24, 19, 21, 14, 3, 10, 2, 13, 11]
MAX_HEAPIFY(A, 0)
print(A)
