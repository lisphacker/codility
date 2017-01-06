# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    for x in A:
        i = abs(x) - 1
        if i != len(A):
            A[i] = -A[i]

    for i, x in enumerate(A):
        if x > 0:
            return i + 1

    return len(A) + 1
