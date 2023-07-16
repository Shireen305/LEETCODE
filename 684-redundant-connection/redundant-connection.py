class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        boss=[i for i in range(len(edges)+1)]
        size=[1]*(len(edges)+1)
        sets=[{i} for i in range(len(edges)+1)]
        t=[]
        not_take=[]
        def find(edge):
            return boss[edge]
        def union(u,v):
            if size[boss[u]]>size[boss[v]]:
                sets[boss[u]]=sets[boss[u]]| sets[boss[v]]
                size[boss[u]]+=size[boss[v]]
                for z in sets[boss[v]]:
                    boss[z]=boss[u]
            else:
                sets[boss[v]]=sets[boss[v]]| sets[boss[u]]
                size[boss[v]]+=size[boss[u]]
                for z in sets[boss[u]]:
                    boss[z]=boss[v]

        for u,v in edges:
            if find(u)!=find(v):
                t.append([u,v])
            else:
                not_take.append([u,v])
            union(u,v)

        return not_take[-1]


