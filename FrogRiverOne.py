# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    tm = [-1] * X
    for i, t in enumerate(A):
        if t <= X and tm[t - 1] == -1:
            tm[t - 1] = i

    for t in tm:
        if t == -1:
            return -1

    return max(tm)
        
