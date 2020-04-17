def numIslands(grid):
    islands = 0
    for i in range(len(grid)):
        grid[i] = list("0" + "".join(grid[i]) + "0")
    if len(grid) < 1:
        return 0
    
    def dfs(r, c):            
        if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c]=='0':
            return       
        grid[r][c] = '0'   
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    rows = len(grid) 
    cols = len(grid[0]) 
    
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            
            if cell == '0':
                continue
            
            if cell == '1':
                islands += 1
                dfs(r, c)
    return islands

grid = [[0 for i in range(5)] for x in range(4)]
for x in range(4):
    grid[x] = list(input())

print(numIslands(grid))