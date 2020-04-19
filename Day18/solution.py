class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: 
            return 0
  
        X, Y = len(grid), len(grid[0])
        lCount = X + Y - 1
        levels = [[] for l in range(lCount)]
        for x in range(X):
            for y in range(Y):
                levels[x+y].append((x,y))
        for i in range(lCount-2, -1, -1):
            for x,y in levels[i]:
                temp = grid[x][y]
                grid[x][y] = float("inf")
                grid[x][y] = temp + min(grid[min(x+1,X-1)][y], grid[x][min(y+1,Y-1)])
                
        return grid[0][0]