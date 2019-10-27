def count_min_substring(inp):
    """Count min length of substring that make up the string."""
    output = -1
    for each in range(2, len(inp) / 2 + 1):
        if inp[:each] * (len(inp) / each) == inp:
            output = each
            break
    return output

print count_min_substring('rerere')
print count_min_substring('ererere')
