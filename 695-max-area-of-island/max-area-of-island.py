class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=set()
        max_count=0
        
        def bfs(r,c):
            count=0
            queue=[(r,c)]
            while(len(queue)):
                i,j=queue.pop(0)
                visited.add((i,j))
                for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=r<row and 0<=c<col:
                        if grid[r][c] == 1 and (r ,c) not in visited:
                            count+=1
                            queue.append((r , c ))
                            visited.add((r, c ))
            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r ,c) not in visited:
                    max_count=max(bfs(r,c)+1,max_count)               
        return max_count