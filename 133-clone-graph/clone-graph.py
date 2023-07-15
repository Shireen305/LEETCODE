"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # if not node:
        #     return node
        # q=[node]
        # visited = {}
        # while q:
        #     curNode=q.pop()
        #     if curNode not in visited: visited[curNode] = Node(curNode.val)
        #     for nghbr in curNode.neighbors:
        #         if nghbr and nghbr not in visited:
        #             visited[nghbr] = Node(nghbr.val)
        #             q.append(nghbr) 
        #         visited[curNode].neighbors.append(visited[nghbr])
        # return visited[node] 
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]

           

               
            

        
        
        
        
        