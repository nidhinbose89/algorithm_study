def equilibrium_idx(arr):
    left_sum = 0  # if sum of array[1:] is zero, eq index is 0
    right_sum = sum(arr)
    for index, elem in enumerate(arr):
        right_sum -= elem
        if left_sum == right_sum:
            return index
        left_sum += elem
    return -1

print equilibrium_idx([10, 20, 10, 15, 15])
print equilibrium_idx([-7, 1, 5, 2, -4, 3, 0])
