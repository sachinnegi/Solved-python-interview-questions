# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,n1,n2):
        if not n1 and not n2:
            return True
        if n1==None or n2==None or n1.val != n2.val:
            return False
        return self.dfs(n1.left,n2.right) and self.dfs(n1.right,n2.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root,root)
        