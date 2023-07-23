class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        last_count = {}
        for j in range(len(s)):
            last_count[s[j]] =j
        
        i=0
        target=0
        length=0
        while i<len(s):
            target=max(target,last_count[s[i]])
            length+=1
            if i==target:
                res.append(length)
                length=0
            i+=1
        return res
            


        
