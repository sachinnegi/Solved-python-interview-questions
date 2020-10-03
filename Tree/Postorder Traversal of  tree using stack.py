# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        node = root
        while stack or node:
            while node:
                result.append(node.val)    #append here only as opposed to inorder traversal
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result
        