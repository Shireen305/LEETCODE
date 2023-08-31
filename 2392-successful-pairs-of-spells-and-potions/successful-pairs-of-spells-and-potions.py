class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res=[]
        potions.sort()
        for spell in spells:
            l=0
            r=len(potions)-1
            while l<=r:
                mid=(l+r)//2
                if spell*potions[mid]>=success:
                    r=mid-1
                else:
                    l=mid+1
            res.append(len(potions)-l)
        return res

        