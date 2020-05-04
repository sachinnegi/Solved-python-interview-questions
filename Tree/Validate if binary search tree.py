class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        def check(root,low=float('-inf'), high = float('inf')):
            if not root:
                return True
            if root.val<=low or root.val>=high:
                return False
            if check(root.left,low,root.val) and check(root.right,root.val,high):
                return True
        return check(root)
