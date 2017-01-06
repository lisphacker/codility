# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    if len(A) < 3:
        return 0
    
    A.sort()

    x, y = A[0:2]

    for z in A[2:]:
        if x + y > z and y + z > x and z + x > y:
            return 1
        x, y = y, z

    return 0

def test1():
    print(solution([10, 2, 5, 1, 8, 20]))

def test2():
    print(solution([10, 50, 5, 1]))
