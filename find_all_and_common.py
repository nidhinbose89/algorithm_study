def find_all(arr_1=[], arr_2=[]):
    arr_1.sort()
    arr_2.sort()
    start_1 = 0
    start_2 = 0
    alls = []
    while start_1 < len(arr_1) and start_2 < len(arr_2):
        if arr_1[start_1] < arr_2[start_2]:
            alls.append(arr_1[start_1])
            start_1 += 1
        elif arr_1[start_1] > arr_2[start_2]:
            alls.append(arr_2[start_2])
            start_2 += 1
        else:
            alls.append(arr_1[start_1])
            start_1 += 1
            start_2 += 1
    alls.extend(arr_1[start_1:])
    alls.extend(arr_2[start_2:])
    return alls


def find_common(arr_1=[], arr_2=[]):
    arr_1.sort()
    arr_2.sort()
    start_1 = 0
    start_2 = 0
    commons = []
    while start_1 < len(arr_1) and start_2 < len(arr_2):
        if arr_1[start_1] < arr_2[start_2]:
            start_1 += 1
        elif arr_1[start_1] > arr_2[start_2]:
            start_2 += 1
        else:
            commons.append(arr_1[start_1])
            start_1 += 1
            start_2 += 1
    return commons
    # When difference between sizes of two given arrays is significant:
    # The idea is to iterate through the shorter array and do a binary search
    # for every element of short array in big array (note that arrays are
    # sorted). Time complexity of this solution is O(min(mLogn, nLogm)).
    # This solution works better than the above approach when ratio of
    # larger length to smaller is more than logarithmic order.


arr_1 = [1, 9, 3, 4, 18, 5, 7]
arr_2 = [2, 3, 5, 12, 6, 9]
print "Array 1:", arr_1
print "Array 1:", arr_2
print "Find all elements in two given arrays"
print find_all(arr_1=arr_1, arr_2=arr_2)
print "Find common elements in two given arrays"
print find_common(arr_1=arr_1, arr_2=arr_2)
