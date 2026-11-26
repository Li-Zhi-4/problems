class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                land = deque()
                if grid[r][c] == "1" and (r,c) not in seen:
                    land.append((r,c))
                    seen.add((r,c))
                    islands += 1
                    while land:
                        (row, col) = land.popleft()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):   # down, up, right, left
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in seen:
                                seen.add((nr, nc))
                                land.append((nr, nc))
        return islands