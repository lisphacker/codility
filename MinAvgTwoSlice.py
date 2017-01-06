# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def div(a, b):
    return float(a) / float(b)

def solution(A):
    min_sum_so_far = min_sum_ending_here = A[0] + A[1]
    min_len_so_far = min_len_ending_here = 2
    min_start_so_far = min_start_ending_here = 0

    for i in range(2, len(A)):
        l = A[i - 1]
        x = A[i]

        if div(x + l, 2) < div(min_sum_ending_here + x, min_len_ending_here + 1):
            min_sum_ending_here = x + l
            min_len_ending_here = 2
            min_start_ending_here = i - 1
        else:
            min_sum_ending_here = min_sum_ending_here + x
            min_len_ending_here += 1

        if div(min_sum_so_far, min_len_so_far) > div(min_sum_ending_here, min_len_ending_here):
            min_sum_so_far = min_sum_ending_here
            min_len_so_far = min_len_ending_here
            min_start_so_far = min_start_ending_here

    return min_start_so_far
