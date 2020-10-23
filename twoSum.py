class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums:
                if i != nums.index(difference):
                    return [i, nums.index(difference)]
