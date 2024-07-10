class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            # calculate the sum of squares of the no
            n = self.sumofsquares(n)
            if n==1:
                return True
        # not at all a happy no
        return False
    def sumofsquares(self,n:int)->int:
        output = 0
        while n:
            # taking each digit and add it to the output
            digit = n % 10
            digit = digit ** 2
            output += digit
            # update the value n
            n = n//10
        return output
