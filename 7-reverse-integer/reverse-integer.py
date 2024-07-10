class Solution:
    def reverse(self, x: int) -> int:
        min = -2**31
        max = 2**31
        res = 0
        while x:
            # extracting each digit in x
            digit = int(math.fmod(x, 10))
            # chopped off the digit
            x = int(x/10)
            # result out of bounds
            # 1. compare other digits except the ones digit
            # 2. other digits are equal and ones place digit is >=
            if (res>max//10 or
                (res == max//10 and digit>=max%10)):
                return 0
            if (res<min//10 or
                (res == min//10 and digit<=min%10)):
                return 0
            # finally take that digit and add it to result
            res = (res*10)+digit
        return res