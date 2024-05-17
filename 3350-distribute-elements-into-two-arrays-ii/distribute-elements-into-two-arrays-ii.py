from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        arr1 = SortedList([nums[0]])
        
        arr2 = SortedList([nums[1]])
        
        a1 = [nums[0]]
        a2 = [nums[1]]
        
        
        N = len(nums)
        for i in range(2,N):
            
            cur = nums[i]
            
            c1 = len(arr1)- bisect.bisect(arr1,cur)
            c2 = len(arr2)- bisect.bisect(arr2,cur)

            if c1 > c2:
                arr1.add(cur)
                a1.append(cur)
            elif c2 > c1:
                arr2.add(cur)
                a2.append(cur)
            elif len(arr1) < len(arr2):
                arr1.add(cur)
                a1.append(cur)
            elif len(arr2) < len(arr1):
                arr2.add(cur)
                a2.append(cur)
            else:
                arr1.add(cur)
                a1.append(cur)
        

        return a1+a2