def longestSubarrayWithSumK(arr: [int], k: int) -> int:
    # Write your code here
    n = len(arr)
    h_map = {}
    cur_sum = 0
    maxlen=0
    # we need the length
    for i in range(n):
        cur_sum+=arr[i]
        if cur_sum==k:
            maxlen = max(maxlen, i+1)
        if cur_sum not in h_map:
            h_map[cur_sum] = i
        print(h_map)
        # main result computation
        remaining = cur_sum-k
        print(remaining)
        if remaining in h_map:
            maxlen = max(maxlen, i-h_map.get(remaining, 0))
            print(maxlen)
    print(maxlen)
longestSubarrayWithSumK([1, 2, 3, 1, 1, 1, 1], 3)