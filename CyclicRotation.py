# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    l = len(A)
    if l == 0:
        return A
        
    k2 = K % l
    if k2 == 0:
        return A
        
    B = [0] * len(A)
    B[0:k2] = A[(l - k2):]
    B[k2:] = A[0:(l - k2)]
    
    return B
