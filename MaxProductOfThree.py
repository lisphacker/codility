# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    A.sort(reverse=True)
    return max(A[0] * A[1] * A[2], A[0] * A[-1] * A[-2])

