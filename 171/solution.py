"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ls = map(ord, s)
        num = 0
        index = len(s)
        for i in xrange(len(ls)):
            ls[i] -= 64
            ls[i] = ls[i] * (26 ** (index - 1))
            index -= 1
        num = sum(ls)
        return num