class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, i, j, grid):
        # Row checking and column chechking
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                self.dfs(i - 1, j, grid)
                self.dfs(i + 1, j, grid)
                self.dfs(i, j + 1, grid)
                self.dfs(i, j - 1, grid)
        else:
            return
            

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    self.count += 1
                    self.dfs(i, j, grid)

        return self.count