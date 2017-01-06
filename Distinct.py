# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    A.sort()

    if len(A) == 0:
        return 0
    
    c = 1
    l = A[0]

    for v in A[1:]:
        if v != l:
            c += 1
            l = v

    return c

