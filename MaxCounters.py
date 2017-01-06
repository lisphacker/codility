# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    counters = [0] * N

    mx = 0
    lastmx = 0

    start = -1
    for i, x in enumerate(reversed(A)):
        if x == N + 1:
            start = len(A) - i - 1
            break

    for i in range(start + 1):
        x = A[i] - 1
        if x < N:
            if counters[x] < lastmx:
                counters[x] = lastmx
            counters[x] += 1
            if counters[x] > mx:
                mx = counters[x]
        else:
            lastmx = mx

    counters = [mx] * N
    
    for i in range(start + 1, len(A)):
        x = A[i] - 1
        if x < N:
            counters[x] += 1

    return counters
