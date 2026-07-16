# https://leetcode.com/problems/next-permutation/description/
from itertools import permutations
class Solution(object):
    def nextPermutation(self, nums):
        a=tuple(nums)
        nums.sort()
        per=list(permutations(nums))
        if a==per[-1]:
            return list(per[0])
        else :
            for i in range(len(per)):
                if a==per[i]:
                    return list(per[i+1])
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

a=list(map(int,input().split()))
print(Solution().nextPermutation(a))