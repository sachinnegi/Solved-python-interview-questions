# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_val = -float('inf')
        def maxPath(node):
            if node == None:
                return 0
            left = max(0, maxPath(node.left))   # taking only max of left or 0 going tille the end of left 
            right = max(0, maxPath(node.right))  # 0 or max right
            
            self.max_val = max(self.max_val, node.val + left + right) # max value at  this root node including value coming from its left and right child
            
            return node.val+ max(left,right) # now returning either node+left or node+right since only a single path value can be taken upward

        maxPath(root)
        return self.max_val
            
            
        
