class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            weight,target=heapq.heappop(minHeap)
            if target in visit:
                continue
            visit.add(target)
            t=weight
            for tar,w in graph[target]:
                if tar not in visit:
                    heapq.heappush(minHeap, (weight + w, tar))

        if len(visit)==n:
            return t
        else:
            return -1

