class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        visited=set()
        count=0
        
        visited = set()
        island = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or (r,c) in visited or board[r][c]=='X':
                return
            visited.add((r,c))
            for x,y in [(r,c-1),(r,c+1),(r-1,c),(r+1,c)]:
                dfs(x,y)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in visited and i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
                    dfs(i,j)
        print(visited)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited and i!=0 and i!=len(board)-1 and j!=0 and j!=len(board[0])-1:
                    board[i][j]='X'
                    dfs(i,j)
        
        return island
                         
    