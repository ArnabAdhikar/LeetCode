# Divide Two Integers
# https://www.youtube.com/watch?v=pBD4B1tzgVc
# https://leetcode.com/problems/divide-two-integers/description/?source=submission-ac

import sys
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # edge cases
        if dividend==divisor:
            return 1
        # dealing with the sign
        sign = True
        if dividend>=0 and divisor<0:
            sign = False
        if dividend<0 and divisor>0:
            sign = False
        # infinity case
        if divisor==0:
            return sys.maxsize
        # performing the operations excluding the sign
        ans = 0
        n = abs(dividend) # numerator
        d = abs(divisor) # denominator
        while n>=d:
            count = 0
            while n>=(d*(2**(count+1))):
                count+=1
            ans+=(2**count)
            # reseting the numerator
            n = n-(d*(2**count))
        # dealing with the intiger storage limit
        if ans>=2**31 and sign == True:
            # returning the maximum limit
            return (2**31)-1
        if ans>=2**31 and sign == False:
            # returning the minimum limit
            return -(2**31)
        if sign==True:
            return ans
        elif sign==False:
            return -1*ans
