# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    min_sum_so_far = min_sum_ending_here = A[0]
    min_len_so_far = min_len_ending_here = 1

    for x in A[1:]:
        if x < (min_sum_ending_here + x) / (min_len_ending_here + 1):
            min_sum_ending_here = x
            min_len_ending_here = 1
        else:
            min_sum_ending_here = min_sum_ending_here + x
            min_len_ending_here += 1

        if min_sum_so_far / min_len_so_far > min_sum_ending_here / min_len_ending_here:
            min_sum_so_far = min_sum_ending_here
            min_len_so_far = min_len_ending_here
            

    return min_sum_so_far / min_len_so_far
