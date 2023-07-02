class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start,target, subset):
            if subset not in res and target==0:
                res.append(subset[:])
            prev = -1
            for i in range(start,len(candidates)):
                if target<0:
                    return 
                if prev==candidates[i]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,target-candidates[i],subset)
                subset.pop()
                prev = candidates[i]
            return res     
        res = []
        candidates.sort()
        backtrack(0,target, [])
        return res