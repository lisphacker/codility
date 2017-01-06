# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):
    amk = A % K
    bmk = B % K
    
    a = A if amk == 0 else A + K - amk
    b = B

    r = int((b - a) / K) + 1
    return r
