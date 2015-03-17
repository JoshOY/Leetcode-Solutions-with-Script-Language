"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        #elif n == 3:
        #    return 5
        else:
            result = 0
            for i in range(0, n):
                result += self.numTrees(i) * self.numTrees(n - 1 - i)
            return result

if __name__ == "__main__":
    s = Solution()
    print s.numTrees(3)
    print s.numTrees(4)