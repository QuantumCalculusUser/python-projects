# https://leetcode.com/problems/divide-two-integers/description/
def multiplyfunction(a, b):
    c=0
    for i in range(b):
        c+=a
    return c
class Solution(object):
    def divide(self, dividend, divisor):
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            index=-1
            while True:
                if -(multiplyfunction(index,-divisor)) > dividend:
                    break
                index-=1
            return index+1
        else:
            index=0
            while True:
                if multiplyfunction(divisor, index) > dividend:
                    break
                index+=1
            return index-1
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        