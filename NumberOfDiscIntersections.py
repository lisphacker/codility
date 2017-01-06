# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def compare(n1, n2):
    if n1[0] == n2[0]:
        if n1[1] == 'IN':
            return -1
        elif n2[1] == 'IN':
            return 1
        else:
            return 0
    else:
        return cmp(n1[0], n2[0])
    
def solution(A):
    nodes = []
    for i, r in enumerate(A):
        nodes.append((i - A[i], 'IN', i))
        nodes.append((i + A[i], 'OUT', i))

    nodes.sort(cmp=compare)

    intersections = 0
    disc_count = 0

    for loc, direc, i in nodes:
        if direc == 'IN':
            disc_count += 1
            if disc_count >= 2:
                intersections += (disc_count - 1)
        else:
            disc_count -= 1

        if intersections > 10000000:
            return -1

    return intersections

        
    
    
def test1():
    print(solution([1, 5, 2, 1, 4, 0]))

def test2():
    print(solution([1, 1, 1]))
    
def test3():
    print(solution([0, 2, 4]))
