# Longest substring without repeating characters

def uniqueSubstrings(s: str) :
    char_set = set()
    left = 0
    finals = 0
    for right in range(len(s)):
        # if there is any duplicate element, pop the element from the set
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        finals = max(finals, right-left+1)
    return finals
