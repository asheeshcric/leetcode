class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            queue = [(row, col)]
            while len(queue) > 0:
                r, c = queue.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    n_r, n_c = r + dr, c + dc
                    if (
                        n_r in range(rows) and n_c in range(cols) and grid[n_r][n_c] == "1"
                    ) and (n_r, n_c) not in visited:
                        queue.append((n_r, n_c))
                        visited.add((n_r, n_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands