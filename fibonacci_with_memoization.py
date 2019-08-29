out = {0: 0, 1: 1}


def fibr(n):
    if n in out:
        return out[n]
    out[n] = fibr(n - 1) + fibr(n - 2)
    return out[n]


def fib_bottom_up(n):
    if n == 0 or n == 1:
        return 1

    nums = []
    nums.append(1)
    nums.append(1)
    for each_idx in xrange(2, n + 1):
        nums.append(nums[each_idx - 1] + nums[each_idx - 2])
    return nums[n]


if __name__ == '__main__':
    for x in range(10):
        print x, fib_bottom_up(x)

    # for x in range(10):
    #     print x, fibr(x)
