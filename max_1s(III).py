# maximum no of 1s-> 111

def longestSubSeg(nums, n, k):
    #   Write your code here.
    left = 0
    right = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            k-=1
        # if k<0-> move the left part of the window-> try and remove the extra 0s
        # slide the window
        if k<0:
            # if the left one was zero then we adjust K
            if nums[left] == 0:
                k+=1
            left+=1
    return right-left+1
