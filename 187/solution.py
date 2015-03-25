"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
"""
import collections

class Solution:
# @param s, a string
# @return a list of strings
def findRepeatedDnaSequences(self, s):
    c = collections.Counter(s[i:i+10] for i in range(len(s)))
    return [k for k in c if c.get(k) > 1]