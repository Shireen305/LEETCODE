class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=[str(num) for num in nums]
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums.sort(key=cmp_to_key(compare))
        #print(nums)
        largest_num = ''.join(nums)
        return "0" if largest_num[0] == "0" else largest_num


        