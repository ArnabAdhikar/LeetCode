class Solution:
    def sumSubarrayMins(self, asteroids) -> int:
        # Write your code here.
        stack = []
        for i in asteroids:
            # there will be collision
            # incomming=-ve
            # top=+ve
            while stack and stack[-1]>0 and i<0:
                temp = stack[-1]+i
                # -ve asteroid wins
                if temp<0:
                    stack.pop()
                    
                # +ve asteroid wins
                elif temp>0:
                    # i should be destroid
                    i= 0
                # both are destroid
                else:
                    i = 0
                    stack.pop()
            if i:
                stack.append(i)
        return stack
