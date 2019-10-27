

def arrayManipulation(n, queries):
    """Prefix-sum application."""

    def max_sub_sum(arr):
        """Kadanes'  Algo."""
        max_sum = out_max_sum = arr[0]
        index = 1
        while index < len(arr):
            max_sum = max(arr[index], max_sum + arr[index])
            if max_sum > out_max_sum:
                out_max_sum = max_sum
            index += 1
        return out_max_sum
    out_arr = [0] * (n + 1)
    for each_q in queries:
        q_start, q_end, to_add = each_q
        out_arr[q_start - 1] += to_add
        out_arr[q_end] -= to_add
    return max_sub_sum(out_arr)


array_size = 10
arr = (
    [1, 6, 8],
    [3, 5, 7],
    [1, 8, 1],
    [5, 9, 15],
)


print arrayManipulation(n=array_size, queries=arr)

array_size = 5
arr = (
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100],
)

print arrayManipulation(n=array_size, queries=arr)
