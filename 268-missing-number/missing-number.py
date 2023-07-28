class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=len(nums)
        sum=ans*(ans+1)//2
        for n in nums:
            sum-=n
        return sum