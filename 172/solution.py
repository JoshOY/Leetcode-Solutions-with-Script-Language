"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        return 0 if n < 5 else n / 5 + self.trailingZeroes(n / 5)

if __name__ == "__main__":
    s = Solution()
    print s.trailingZeroes(5)
    print s.trailingZeroes(100)
