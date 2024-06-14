class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        # starting from the end => reversing the input string
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            # one of the string is out of bounds
            digita = ord(a[i])-ord("0") if i < len(a) else 0   # convert the strings into integers
            digitb = ord(b[i])-ord("0") if i < len(b) else 0
            # adding them
            total = digita + digitb + carry
            # character that to be added in result string(binary)
            char = str(total % 2)
            res = char + res
            # update the carry
            carry = total // 2
        # carry left over
        if carry:
            res = "1"+res
        return res
