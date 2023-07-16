class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graphCost=defaultdict(list)
        
        for i in range(len(points)):
            x,y=points[i]
            for j in range(i+1,len(points)):
                a,b=points[j]
                cost = abs(x - a) + abs(y - b)
                graphCost[i].append([cost,j])
                graphCost[j].append([cost,i])
        
        res = 0
        visit = set()
        minH = [[0, 0]]  
        while len(visit) < len(points):
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in graphCost[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res


            

