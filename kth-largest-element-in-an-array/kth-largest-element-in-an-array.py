class Solution:
    def selectrand(self,k,nums):
        pivot=random.choice(nums)
        less=[x for x in nums if x<pivot]
        equal=[x for x in nums if x==pivot]
        greater=[x for x in nums if x>pivot]
        if k<len(less):
            return self.selectrand(k,less)
        if k>=len(less) and k<len(less)+len(equal):
            return -pivot
        else:
            return self.selectrand(k-len(less)-len(equal),greater)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_inverse=[-x for x in nums]
        return self.selectrand(k-1,nums_inverse)
        

