class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digit[i] = 0
            else:
                digits[i] += 1
                return digits

    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        for i in range(n-1, -1, -1):
            if digits[i] += 1:
                return digits
            digits[i] = 0
