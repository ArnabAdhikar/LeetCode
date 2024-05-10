# subarray with a given sum
# https://www.youtube.com/watch?v=fFVZt-6sgyo

def findAllSubarraysWithGivenSum(arr, k):
    # Write your code here.
    finals = 0
    cursum = 0
    mydict = {0:1}
    for i in arr:
        cursum+=i
        diff = cursum-k
        # if diff doesnt exist, just return 0
        finals+=mydict.get(diff, 0)
        # pushing the value in the hash map
        mydict[cursum] = 1+mydict.get(cursum, 0)
    return finals
