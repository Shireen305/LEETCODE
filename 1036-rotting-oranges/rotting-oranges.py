class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=set()
        count=0
        count_no=0
        q=[]
        
        def bfs(r,c,count_no):
            i,j=r,c
            for r,c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=r<row and 0<=c<col:
                    if grid[r][c] == 1:
                        count_no-=1
                        grid[r][c] = 2
                        q.append((r , c ))
            return count_no
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count_no+=1
                if grid[r][c]==2:
                    q.append((r,c))

        while count_no>0 and q:
            for _ in range(len(q)):
                r,c=q.pop(0)
                count_no=bfs(r, c,count_no)
            count+=1  
        
        if count_no==0:
            return count
        else:
            return -1    
        # q = collections.deque()
        # fresh = 0
        # time = 0

        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2:
        #             q.append((r, c))

        # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # while fresh > 0 and q:
        #     length = len(q)
        #     for i in range(length):
        #         r, c = q.popleft()

        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc
        #             # if in bounds and nonrotten, make rotten
        #             # and add to q
        #             if (
        #                 row in range(len(grid))
        #                 and col in range(len(grid[0]))
        #                 and grid[row][col] == 1
        #             ):
        #                 grid[row][col] = 2
        #                 q.append((row, col))
        #                 fresh -= 1
        #     time += 1
        # return time if fresh == 0 else -1            
        