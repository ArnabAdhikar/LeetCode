class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points=sorted(points,key =lambda x:x[0])
        ans=0
        i=0
        while(i<len(points)):
            start=i
            if(i<len(points) and points[i][0]-points[start][0]<=w):
                while(i<len(points) and points[i][0]-points[start][0]<=w):
                    i+=1
            else:
                i+=1
            ans+=1
        return ans
