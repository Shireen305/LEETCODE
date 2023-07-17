class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d=[math.inf]*n
        d[src]=0
        for i in range(k+1):
            tmpPrices = d.copy()
            for s,dest,p in flights:
                if d[s] == math.inf:
                    continue
                if tmpPrices[dest]>d[s]+p:
                    tmpPrices[dest]=d[s]+p
            d=tmpPrices
        if d[dst]==math.inf:
            return -1
        else:
            return d[dst]
        # prices = [float("inf")] * n
        # prices[src] = 0

        # for i in range(k + 1):
        #     tmpPrices = prices.copy()

        #     for s, d, p in flights:  # s=source, d=dest, p=price
        #         if prices[s] == float("inf"):
        #             continue
        #         if prices[s] + p < tmpPrices[d]:
        #             tmpPrices[d] = prices[s] + p
        #     prices = tmpPrices
        # return -1 if prices[dst] == float("inf") else prices[dst]