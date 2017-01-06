# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    y = Y - X

    r = y % D
    j = int(y / D)

    return j if r == 0 else j + 1
