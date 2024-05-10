# permutations in string
# https://leetcode.com/problems/permutation-in-string/
# https://www.youtube.com/watch?v=UbyhOgBN834

import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashtable = defaultdict(int)
        running_hashtable = defaultdict(int)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            hashtable[s1[i]]+= 1
            if i < len(s1)-1:
                running_hashtable[s2[i]] += 1
        l = 0
        for j in range(len(s1)-1,len(s2)):
            running_hashtable[s2[j]] += 1
            flag = True
            for k,v in running_hashtable.items():
                
                if v>0:
                    if hashtable.get(k,0) != v:
                        flag = False
                        break 
                else:
                    if hashtable[k] > 0:
                        flag = False
                        break 
            if flag:
                return True
            running_hashtable[s2[l]] -= 1
            l += 1
        return False
