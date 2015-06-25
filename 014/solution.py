"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        ret = ''
        ret_max_len = min(map(len, strs))
        for i in xrange(ret_max_len):
            ch = strs[0][i]
            same = True
            for str in strs:
                if ch == str[i]:
                    continue
                else:
                    same = False
                    break
            if same:
                ret += ch
            else:
                break
        return ret