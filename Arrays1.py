def solution(A, K):
    N = len(A)
    #B=A.copy()
    B = [None] * N
    for i in range(0, N):
        B[(i+K)%N] = A[i]
    return B
    pass


def cyclic_array_rotation(A, K):
    N = len(A)
    B = [None] * N
    for i in range(0, N):
        B[(i+K) % N] = A[i]
    
    print("Original Array:", A)
    print("Rotated Array:", B)
    
    return B

# Example usage
A = [3, 8, 9, 7, 6]
K = 2
result = cyclic_array_rotation(A, K)