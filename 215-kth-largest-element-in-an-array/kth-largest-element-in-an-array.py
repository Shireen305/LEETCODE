class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-j for j in nums]
        print(neg)
        def kselect(num, k):
            x = random.choice(num)
            L,E,G = [], [], []
            for i in num:
                if i < x:
                    L.append(i)
                elif i > x:
                    G.append(i)
                else:
                    E.append(x)
            if k < len(L):
                return kselect(L, k)
            elif k >= len(L) and k < (len(L)+len(E)):
                return -x
            else:
                return kselect(G, k-len(L)-len(E))
        return kselect(neg, k-1)
        

