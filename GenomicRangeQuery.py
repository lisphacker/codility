# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, P, Q):
    N = len(S)

    lastIdx = dict()
    lastIdx['A'] = [-1] * N
    lastIdx['C'] = [-1] * N
    lastIdx['G'] = [-1] * N

    scores = {'A':1, 'C':2, 'G':3}
    ordered_nuc = 'GCA'

    for i, c in enumerate(S):
        
        if i != 0:
            for c2 in lastIdx:
                lastIdx[c2][i] = lastIdx[c2][i - 1]
                      
        if c != 'T':
            lastIdx[c][i] = i

    impact_factors = [0] * len(P)

    for i, (p, q) in enumerate(zip(P, Q)):
        minscore = 4

        for nuc in ordered_nuc:
            if p == 0:
                if lastIdx[nuc][q] != -1:
                    minscore = scores[nuc]
            elif lastIdx[nuc][p - 1] != lastIdx[nuc][q]:
                minscore = scores[nuc]

        impact_factors[i] = minscore

    return impact_factors
        
        

def test1():
    print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
    
def test2():
    print(solution('C', [0], [0]))

def test3():
    print(solution('CAGCCTA', [1], [4]))

def test4():
    print(solution('GGCGG', [0], [1]))

