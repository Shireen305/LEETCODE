class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        def calculate(i,res):
            if i==n:
                if res not in nums:
                    return res
                else:
                    return None
            k=calculate(i+1,res+"0")
            if k:
                return k
            k=calculate(i+1,res+"1")
            if k:
                return k   
        return calculate(0,"")
            




        