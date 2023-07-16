class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        count=[0]*(numCourses)
        total=0
        for course,pre in prerequisites:
            graph[pre].append(course)
            count[course]+=1
            total+=1
        visited=[]
        #print(graph)
        for i in range(len(count)):
            if count[i]==0:
                visited.append(i)
        #print(graph)
        if not visited:
            return False
            
        for pre in visited:
            for course in graph[pre]:
                print(course)
                count[course]-=1
                total-=1
                if count[course]==0:
                    visited.append(course)
            #visited.pop(0)
            if not visited and total!=0:
                return False
        
        if total!=0:
            return False
        return True
                

        
