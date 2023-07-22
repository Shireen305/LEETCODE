class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                max_sum[i]=nums[i]
            else:
                if max_sum[i-1]+nums[i]>nums[i]:
                    max_sum[i]=max_sum[i-1]+nums[i]
                else:
                    max_sum[i]=nums[i]
        return max(max_sum)
                    