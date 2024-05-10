# Shortest Source to Destination Path

#User function Template for python3

class Solution:
    def shortestDistance(self, rows, cols, grid, target_row, target_col):
        # BFS
        # if the starting point or the destination point is blocked there is no valid path.
        if grid[0][0] == 0 or grid[target_row][target_col] == 0:
            return -1
        path_length = 0
        queue = [[0,0]]

        while queue:
            # to store the next level nodes
            temp_queue = []
            for row, col in queue:
                # Check if the current node is out of bounds or is a blocked cell
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                    continue
                # If the current node is the destination
                if row == target_row and col == target_col:
                    return path_length
                # Mark the current node as visited(blocked)
                grid[row][col] = 0
                # modify the temporary queue, for visiting the neighbourours
                # movement in all the 4 directions
                temp_queue.extend([[row, col - 1], [row - 1, col], [row + 1, col], [row, col + 1]])
            # update the queue and the length of the path
            queue = temp_queue
            path_length += 1
        # If no path is found, return -1
        return -1
     
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
