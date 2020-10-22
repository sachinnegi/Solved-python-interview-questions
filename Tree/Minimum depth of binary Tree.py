'''
Time Comp -> O(num of nodes)
Space Comp. -> O(h)   where h can be equal to n in worst case of skewed tree
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1+ self.dfs(root.right)
        if not root.right:
            return 1+ self.dfs(root.left)
        return 1+ min( self.dfs(root.left), self.dfs(root.right))
    
    def minDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
        
        
