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

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        rtn = []
        addrow = []
        row = 0
        while numRows > row:
            row += 1
            addrow = []
            for i in range(row):
                if i == 0 or i == row - 1:
                    addrow.append(1)
                else:
                    addrow.append(rtn[row - 2][i - 1] + rtn[row - 2][i])
            rtn.append(addrow)
        return rtn
