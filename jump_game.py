# Jump Game
# https://leetcode.com/problems/jump-game/description/
# https://www.youtube.com/watch?v=Yan0cv2cLy8

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # initializing the goal
        goal = len(nums)-1
        # traversal from the backwords
        for i in range(len(nums)-1, -1, -1):
            # we can reach the goal
            if i+nums[i] >= goal:
                # shift the goal
                goal = i
        if goal==0:
            return True
        else:
            return False
