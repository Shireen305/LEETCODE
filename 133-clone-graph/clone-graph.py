"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        q=[node]
        visited = {}
        while q:
            curNode=q.pop()
            if curNode not in visited: visited[curNode] = Node(curNode.val)
            for nghbr in curNode.neighbors:
                if nghbr and nghbr not in visited:
                    visited[nghbr] = Node(nghbr.val)
                    q.append(nghbr) 
                visited[curNode].neighbors.append(visited[nghbr])
        return visited[node] 
           

               
            

        
        
        
        
        