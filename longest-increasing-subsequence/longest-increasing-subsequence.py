class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s=[1]*len(nums)
        for i in range(len(nums)):
            s[i]=1
            for j in range(i):
                if nums[j]<nums[i] and s[i]<s[j]+1:
                    s[i]=s[j]+1
        return max(s)