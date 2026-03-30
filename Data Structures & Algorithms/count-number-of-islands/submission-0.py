class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque() # double-ended queue
            visit.add((r,c)) # add the cell on the grid
            q.append((r,c)) # append it to queue

            while q:
                row, col = q.popleft() # use plain pop to make it DFS
                directions = [[1,0],[-1,0],[0,1],[0,-1]] # down, up, right, left

                for dr,dc in directions:
                    r,c = row+dr, col+dc # checking neighbors in the directions
                    # vertical check, horizontal check to see if cell is within the grid, then checking if it is an island and not been visited
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit):
                        q.append((r,c)) # add to queue
                        visit.add((r,c)) # mark visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit: # unvisited island
                    bfs(r,c) # check for neighbors
                    islands += 1 
        
        return islands