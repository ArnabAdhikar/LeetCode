# sum of 2 integers
# https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        # works both as while loop and single value check 
        while (b & mask) > 0:
            # first calculate carry before a and b gets modified
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        # handles overflow
        if b > 0:
            return (a & mask)
        else:
            return a

