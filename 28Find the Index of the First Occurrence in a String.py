# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        