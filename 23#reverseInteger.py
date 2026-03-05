class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        x = abs(x)

        digits = list(map(int, str(x)))

        left = 0
        right = len(digits) - 1

        while left < right:
            digits[left] , digits[right] = digits[right], digits[left]
            left += 1
            right -= 1

        result = 0
        for digit in digits:
            result = result*10+digit

        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result