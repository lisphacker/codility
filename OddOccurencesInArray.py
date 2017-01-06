# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    ar = sorted(A)

    if len(A) == 1:
        return A[0]
    
    for i in range(0, len(ar) - 1, 2):
        if ar[i] != ar[i + 1]:
            return ar[i]

    return ar[-1]
