class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        stack=0
        for c in s:
            if c=='[':
                stack+=1
            else:
                if stack==0:
                    count+=1
                else:
                    stack-=1
        
        return (count+1)//2

            

