class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Left pointer starts at 0
        left = 0  
        # Right pointer starts at the integer square root of c
        right = int(c**0.5)  
        while left <= right:
            curr_sum = left * left + right * right  # Calculate sum of squares of the two pointers
            if curr_sum == c:
                return True  # If sum equals c, return true
            elif curr_sum < c:
                left += 1  # If sum is less than c, move left pointer right
            else:
                right -= 1  # If sum is greater than c, move right pointer left
        
        return False  # If no such pair is found, return false
