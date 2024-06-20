class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        seen_map = {}
        count = 0
        for hour in hours:
            rem = hour % 24
            complement = (24 - rem) % 24
            if complement in seen_map:
                count += seen_map[complement]
            seen_map[rem] = seen_map.get(rem, 0) + 1
        return count
