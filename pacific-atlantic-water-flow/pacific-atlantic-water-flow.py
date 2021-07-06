class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visit_pac, visit_atl = set(), set()

        def dfs(r, c, visit, previous_height):
            # Need to check if it has already been visited or (r, c) is out of bounds or the current height is less than the previous height or not
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or heights[r][c] < previous_height
            ):
                # This cell cannot flow to the oceans
                return
            
            # Add the current cell to the visit set as it can flow to one of the oceans
            visit.add((r, c))
            # Do DFS on all four sides of the current cell
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        # When visiting first row and last row
        for c in range(COLS):
            # DFS for first row for pacific
            dfs(0, c, visit_pac, heights[0][c])
            # DFS for last row for atlantic
            dfs(ROWS - 1, c, visit_atl, heights[ROWS - 1][c])

        # When visiting first column and last column
        for r in range(ROWS):
            # DFS for first column for pacific
            dfs(r, 0, visit_pac, heights[r][0])
            # DFS for last column for atlantic
            dfs(r, COLS - 1, visit_atl, heights[r][COLS - 1])

        # Find intersection of both sets
        result = []
        # print(f'Atlantic\n{visit_atl}')
        # print(f'Pacific\n{visit_pac}')
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in visit_atl and (row, col) in visit_pac:
                    result.append([row, col])

        return result