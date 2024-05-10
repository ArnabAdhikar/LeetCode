# maximum sub array sum
# Kaden's Algorithm

import sys
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    cur_sum = 0
    finals = -sys.maxsize-1
    n = len(arr)
    for i in range(n):
        cur_sum+=arr[i]
        if cur_sum>finals:
            finals=cur_sum
        if cur_sum<0:
            cur_sum=0
    return max(finals, 0)
def takeInput() :
    n =  int(input())
    if(n == 0) :
        return list(), n
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n
#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
