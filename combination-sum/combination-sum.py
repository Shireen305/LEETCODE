class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_comb(start,target,comb):
            if target==0:
                res.append(comb[:])   
            for i in range(start,len(candidates)):
                if target<0:
                    return 
                comb.append(candidates[i])
                find_comb(i,target-candidates[i],comb)
                comb.pop()
            return res     
        res = []
        find_comb(0,target,[])
        return res

            
