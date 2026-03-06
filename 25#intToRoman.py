# leet code 12. integer to roman
# https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result