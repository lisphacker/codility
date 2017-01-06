# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    left = A[0]
    right = sum(A[1:])
    mn = abs(left - right)

    for x in A[1:-1]:
        left += x
        right -= x

        diff = abs(left - right)
        if diff < mn:
            mn = diff

    return mn
