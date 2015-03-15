"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

import operator

def C(n, k):  
    return reduce(operator.mul, range(n - k + 1, n + 1)) / reduce(operator.mul, range(1, k + 1))

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	if numRows == 0:
    		return []
    	tri = [[1]]
        for row_index in xrange(numRows - 1):
            tri.append([1])
            for i in range(row_index + 1):
                tri[row_index + 1].append(C(row_index + 1, i + 1))
        return tri

if __name__ == "__main__":
    s = Solution()
    print s.generate(1)