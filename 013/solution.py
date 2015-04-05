"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        if not s:
            return 0
        numdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        result = 0
        lastch = ''
        for ch in s:
            result += numdic[ch]
            if lastch == 'I' and (ch == 'V' or ch == 'X'):
                result -= 2
            elif lastch == 'X' and (ch == 'L' or ch == 'C'):
                result -= 20
            elif lastch == 'C' and (ch == 'D' or ch == 'M'):
                result -= 200
            lastch = ch
        return result