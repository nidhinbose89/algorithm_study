# Good morning! Here's your coding interview problem for today.
# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def find_sum_items(arr, sum_num):
    s = set()
    for idx, each_item in enumerate(arr):
        the_diff = abs(each_item - sum_num)
        if the_diff in s:
            print the_diff, 'sd'
            return True
        s.add(each_item)
        print s
    return False


print find_sum_items(arr=[10, 15, 3, 7], sum_num=17)
