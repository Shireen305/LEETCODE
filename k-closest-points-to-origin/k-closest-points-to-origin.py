class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_dict=[]
        p2=[0,0]
        for i in range(len(points)):
            ans=dist(points[i],p2)
            point_dict.append([ans,points[i]])
        
        heapq.heapify(point_dict)
        res=[]

        for i in range(k):
            distance,point=heapq.heappop(point_dict)
            res.append(point)

        return res



