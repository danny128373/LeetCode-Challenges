import collections


def find_uniq(arr):
    counter_dict = collections.Counter(arr)
    tuple_dict = [(k, v) for k, v in counter_dict.items()]
    for tup in tuple_dict:
        if tup[1] == 1:
            return tup[0]


print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([7, 7, 7, 7, 7, 7, 6, 7]))
