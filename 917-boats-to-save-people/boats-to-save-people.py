class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        weight=0
        boat=0
        while(left<=right):
           weight=people[left]+people[right]
           if weight>limit:
               right-=1
               boat+=1
           elif weight<=limit:
                right-=1
                left+=1
                boat+=1
        return boat
