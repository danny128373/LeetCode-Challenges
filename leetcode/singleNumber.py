import collections


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = collections.Counter(nums)
    for k, v in nums.items():
        if v == 1:
            return k


print(singleNumber([2, 1, 2]))
