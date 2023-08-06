class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_list=[]
        for num in arr:
            new_list.append(abs(num-x))
        left=0
        right=0
        res=0
        index=0
        min_res=float('inf')
        while(right<=len(new_list)-1):
            res+=new_list[right]
            if right-left==k-1:
                if res<min_res:
                    min_res=res
                    index=left
                res-=new_list[left]
                left+=1
            right+=1
        return arr[index:index+k]

       
        # left = 0
        # right = len(arr) - 1
        
        # while right - left >= k:
        #     if abs(x - arr[left]) > abs(x - arr[right]):
        #         left += 1
        #     else:
        #         right -= 1
        
        # return arr[left:right+1]



