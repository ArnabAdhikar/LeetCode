from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        decreasing_queue = deque()
        answer = []
        for i in range (len(nums)):
            # removing the out of bound
            if decreasing_queue and decreasing_queue[0]==i-k:
                decreasing_queue.popleft()
            # removing the last element from stack if incomming(x)>=top()
            while decreasing_queue and nums[i] >= nums[decreasing_queue[-1]]:
                decreasing_queue.pop()
            decreasing_queue.append(i)
            # putting the answers
            # if the desired window size is reached append the values against the index
            # first window [0-1-2]
            if i>=k-1:
                answer.append(nums[decreasing_queue[0]])
        return answer
