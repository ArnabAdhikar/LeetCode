# Task Scheduler
# https://leetcode.com/problems/task-scheduler/description/
# https://www.youtube.com/watch?v=s8p8ukTyA2I

from typing import List
import Counter
import heapq
import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counting the occurance of each character
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        # converting into heap(max heap)
        heapq.heapify(maxheap)
        time = 0
        q = deque()
        # perform the operation untill the heap or q is non empty
        while maxheap or q:
            # in performing each operation increment the time by 1
            time += 1
            # maxheap is non empty
            if maxheap:
                # get the count
                c = 1+heapq.heappop(maxheap)   #-> processing the task
                # c is non 0=> append to the queue
                if c:
                    q.append([c, time+n])
            # q is non-empty and q(first value-> idle time) completed=> push into the heap
            if q and q[0][1]==time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
