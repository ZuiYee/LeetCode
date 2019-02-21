class Solution:
    def projectionArea(self, grid: 'List[List[int]]') -> 'int':
        M, N = len(grid), len(grid[0])
        rowMAX, colMAX = [0] * M, [0] * N
        xy = sum(0 if grid[i][j] == 0 else 1 for i in range(M) for j in range(N))
        xz = sum(list(map(max, grid)))
        yz = sum(list(map(max, [[grid[i][j] for i in range(M) for j in range(N)]])))
        return xy + xz + yz