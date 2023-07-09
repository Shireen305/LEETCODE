class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        maxnum=1
        minnum=1
        for n in nums:
            if n==0:
                maxnum,minnum=1,1
                continue
            tmp = maxnum* n
            maxnum = max(n * maxnum, n * minnum, n)
            minnum = min(tmp, n * minnum, n)
            res = max(res, maxnum)
        return res