# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    zc = 0
    count = 0

    for c in A:
        if c == 0:
            zc += 1
        else: # c == 1
            count += zc
            if count > 1000000000:
                return -1

    return count
