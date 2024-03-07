class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # path = set()
        path = []
        return self.helper(0, 0, path, grid)

    def helper(self, row, col, path, grid):
        if row == len(grid) - 1 and col == len(grid[len(grid) - 1]) - 1:
            if grid[row][col] == 0: return 1
            else: return 0
        if row >= len(grid) or row < 0: return 0
        if col >= len(grid[len(grid) - 1]) or col < 0: return 0
        if grid[row][col] == 1: return 0
        # print(grid[row][col], row, col, path)
        if (row, col) in path: return 0
        count = 0
        # path.add((row, col))
        path.append((row, col))

        count += self.helper(row + 1, col, path, grid)
        count += self.helper(row - 1, col, path, grid)
        count += self.helper(row, col + 1, path, grid)
        count += self.helper(row , col - 1, path, grid)

        # path.remove((row, col))
        path.pop()

        return count