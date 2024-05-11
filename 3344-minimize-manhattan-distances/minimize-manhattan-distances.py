class Solution:
    def manhattan(self, points: List[List[int]], i: int, j: int) -> int:
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    
    def maxManhattanDistance(self, points: List[List[int]], remove: int = -1) -> Tuple[int]:
        n = len(points)
        maxSum, minSum, maxDiff, minDiff = -inf, inf, -inf, inf
        for i in range(n):
            if i != remove:
                s = points[i][0] + points[i][1]
                d = points[i][0] - points[i][1]
                if s > maxSum:
                    maxSumIndex = i
                    maxSum = s
                if s < minSum:
                    minSumIndex = i
                    minSum = s
                if d > maxDiff:
                    maxDiffIndex = i
                    maxDiff = d
                if d < minDiff:
                    minDiffIndex = i
                    minDiff = d
        return (maxSumIndex, minSumIndex) \
            if max(maxSum - minSum, maxDiff - minDiff) == maxSum - minSum \
            else (maxDiffIndex, minDiffIndex)
    
    def minimumDistance(self, points: List[List[int]]) -> int:
        mi, mj = self.maxManhattanDistance(points)
        return min(
            self.manhattan(points, *self.maxManhattanDistance(points, mi)), # remove mi
            self.manhattan(points, *self.maxManhattanDistance(points, mj)) # remove mj
        )
