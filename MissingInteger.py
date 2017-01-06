# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    found = [False] * len(A)
    for x in A:
        if x <= 0:
            continue
        
        i = x - 1
        if i < len(A):
            found[i] = True

    for i, f in enumerate(found):
        if not f:
            return i + 1

    return len(A) + 1
