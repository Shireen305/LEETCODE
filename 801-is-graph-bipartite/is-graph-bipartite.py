class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        start=0
        visited=set()
        dist={}
        for i in range(len(graph)):
            if graph[i] and i not in visited:
                queue=[i]
                dist[i]=0
                while queue:
                    curr=queue.pop(0)
                    if curr not in visited:
                        visited.add(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in dist:
                            dist[neighbor]=dist[curr]+1
                            queue.append(neighbor)
                        elif dist[neighbor]==dist[curr]:
                            return False      
        return True
        
                
        