def sum_of_intervals(intervals):
    numbers = []
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            numbers.append(i)
    return len(set(numbers))


print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
