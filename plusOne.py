class Solution(object):
    # this one passes 105 out of 109 tests
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

    # this one passes all tests
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        new_number = [0] * (len(digits) + 1)
        new_number[0] = 1
        return new_number
