# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        val=""
        def traversal(root,res,val):
            if root:
                val+=str(root.val) 
                print(val)
            if root:
                traversal(root.left,res,val)
                traversal(root.right,res,val)
            if root and root.left is None and root.right is None:
                res.append(val)
                #print(res)
                #val=""
        traversal(root,res,val)
        sum=0
        print(res)
        for v in res:
            sum+=int(v)
        return sum

           
        
       
        
       

        

        