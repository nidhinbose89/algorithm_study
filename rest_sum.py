# if our input was [1, 2, 3, 4, 5], the expected output would be
# >> [120, 60, 40, 30, 24]


def get_total_mul(arr):
    # return the sum of items multiplied
    result = 1
    for each in arr:
        result = result * each
    return result


# print get_mul_sum([1, 2, 3, 4, 5])
def get_mul_sum_array(arr):
    first_sum = get_total_mul(arr[1:])
    result_array = [first_sum]
    for idx in range(1, len(arr)):
        result_array.append(first_sum / arr[idx] * arr[0])
    print result_array
    return result_array


assert get_mul_sum_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
