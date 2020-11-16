def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    boolean_list = []
    max_num = max(candies)
    for kid in candies:
        if kid + extraCandies < max_num:
            boolean_list.append(False)
        else:
            boolean_list.append(True)
    return boolean_list


print(kidsWithCandies([2, 5, 1, 7, 0], 2))
