
def create_pyramid(base, char):
    out_list = []
    base_arr = [''] * base
    mid_index = (base / 2.0)
    start = int(mid_index)
    end = int(mid_index) + 1
    is_even = (base % 2) == 0
    first_loop = True
    while start >= 0 and end <= base:
        one_arr = base_arr[:]
        one_arr[start:end] = [char] * (end - start)
        out_list.append(one_arr)
        start -= 1
        if is_even and first_loop:
            first_loop = False
            continue
        end += 1
    return out_list

print create_pyramid(6, "A")


# ar = ['A'] * 8
# ar[1:5] = ['*'] * (5 - 1)
# print ar
# 3
[
['', 'A', ''],
['A', 'A', 'A'],
]

# 4
[
['', '', 'A', ''],
['', 'A', 'A', ''],
['A', 'A', 'A', 'A'],
]

# 6
[
['', '', '', 'A', '', ''],
['', '', 'A', 'A', '', ''],
['', 'A', 'A', 'A', 'A', ''],
['A', 'A', 'A', 'A', 'A', 'A']
]

# 7
[
['', '', '', 'A', '', '', ''],
['', '', 'A', 'A', 'A', '', ''],
['', 'A', 'A', 'A', 'A', 'A', ''],
['A', 'A', 'A', 'A', 'A', 'A', 'A'],
]
