# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            result= self.maxDepth(root.left)+self.maxDepth(root.right)
            return max(result,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        else:
            return 0
        
        