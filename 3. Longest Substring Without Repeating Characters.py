# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # def valid(lis):
        #     def val(a):
        #         b=[]
        #         for i in a:
        #             if i not in b:
        #                 b.append(i)
        #             else:
        #                 return False
        #         return True
        #     for i in lis:
        #         if val(i)==True:
        #             return True
        #     return False
        # b=0
        # for i in range(len(s),0,-1):
        #     a=[]
        #     for j in range(len(s)-i+1):
        #         a.append(s[j:j+i])
        #     b=0
        #     if valid(a)==True:
        #         b=i
        #         break
        b=0
        c=list(str(s))
        for i in range(len(s)):
            a=[]
            
            pass
            
        return b
    
# INCOMPLETED