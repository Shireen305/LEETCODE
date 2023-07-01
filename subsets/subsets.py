class Solution:
    # def subset_finder(self,subset,nums,res):
    #     for i in range(len(nums)):
    #         subset.append(nums[i])
    #         return res.append(self.subset_finder(subset,nums[i+1:],res))

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subset=[]
    #     res=[]
    #     return self.subset_finder(subset,nums,res)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            res.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        res = []
        backtrack(0, [])
        return res
        