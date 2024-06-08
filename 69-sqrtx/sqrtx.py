class Solution:
    def mySqrt(self, x: int) -> int:
        # initialize the search space
        l, r = 0, x
        res = 0
        # binary search
        while l<=r:
            # m = (l+r)//2 == l+((r-1)//2)
            m = l+((r-l)//2)
            # equalities
            if m**2 > x:
                # decrease our search space
                r = m - 1
            elif m**2 < x:
                # increase the serach space
                l = m + 1
                # mid value could be the result
                res = m
            else:
                return m
        return res
