import copy

"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        numcpy = copy.deepcopy(num)
        numcpy.sort()
        print numcpy

        r1 = 0
        r2 = len(numcpy) - 1

        while True:
            if numcpy[r1] + numcpy[r2] == target:
                break
            elif numcpy[r1] + numcpy[r2] < target:
                r1 += 1
            elif numcpy[r1] + numcpy[r2] > target:
                r2 -= 1

        num1 = numcpy[r1]
        num2 = numcpy[r2]
        
        index1 = num.index(num1)
        index2 = num.index(num2)

        if index2 == index1:
            index2 += 1
            while num[index2] + num[index1] != target:
                index2 += 1
        
        return (index1 + 1, index2 + 1) if index1 < index2 else (index2 + 1, index1 + 1)