# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,ans):
        if root:
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)
            return ans
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        res=self.inorder(root,ans)
        print(res)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True
        
    

