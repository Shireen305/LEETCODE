class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        visited=set()
        count=0
        
        def bfs(r,c):
            queue=[(r,c)]
            while(len(queue)):
                i,j=queue.pop(0)
                visited.add((i,j))
                for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=r<row and 0<=c<col:
                        if grid[r][c] == '1' and (r ,c) not in visited:
                         queue.append((r , c ))
                         visited.add((r, c ))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r ,c) not in visited:
                    bfs(r,c)
                    count+=1      
        return count
                    
                
            
        



