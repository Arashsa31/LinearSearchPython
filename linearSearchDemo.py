def linear_search(data, search_key):
    for index, value in enumerate(data):
        if value == search_key:
            return index
    return -1

#           0   1   2   3   4   5   6   7   8   9
values = ([35, 73, 90, 65, 23, 86, 43, 81, 34, 58])
print(values)

print(linear_search(values, 23))
print(linear_search(values, 61))
print(linear_search(values, 34))