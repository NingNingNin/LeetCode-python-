class Solution(object):
    def __init__(self):
        self.count =0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        hang = len(grid)
        lie = len(grid[0])
        isvist = [[0] * lie for _ in range(hang)]
       
                        
        def DFS(grid,isvist,i,j):
            isvist[i][j] = 1
            nr, nc = len(grid), len(grid[0])
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1" and isvist[x][y] ==0:
                    DFS(grid,isvist,x,y)

        for i in range(hang):
            for j in range(lie):
                if grid[i][j]== "1" and isvist[i][j] == 0:
                    DFS(grid,isvist,i,j)
                    self.count += 1
                

        return self.count


