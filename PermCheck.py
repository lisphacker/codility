# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    for x in A:
        i = abs(x) - 1
        if i < len(A) and A[i] > 0:
            A[i] = -A[i]

    for x in A:
        if x > 0:
            return 0

    return 1
