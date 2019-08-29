def binary_search(array, element):
    """Binary Search.
        Works only in sorted array.
        start = 0, end = len of array - 1 // index starts at 0
        while start < = end
        keep on finding mid point in array. check
            if element = mid.
            if element GRT mid. - start = mid + 1
            if LST mid element. = end = mid - 1

    """
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) / 2
        if element == array[mid]:
            return "At index: " + str(mid)
        elif element < array[mid]:
            end = mid - 1
        elif element > array[mid]:
            start = mid + 1
    return "Not Found"

print "Binary Search..."
aa = [2, 3, 13, 21, 36, 47, 81, 97]
element_1 = 13
element_2 = 93
print "Find {ele} in {lis}".format(ele=element_1, lis=aa)
print binary_search(aa, element_1)
print "Find {ele} in {lis}".format(ele=element_2, lis=aa)
print binary_search(aa, element_2)
a = xrange(10000000000)
# THIS WILL TAKE A LONG TIME =>>> "999999999 in a"
# ESPECIALLY IF THE ARRAY IS SORTED -- utilize Binary Search
print "Find {ele} in {lis}".format(ele=9999999999, lis="xrange(10000000000)")
print binary_search(a, 9999999999)
print "***End***"
