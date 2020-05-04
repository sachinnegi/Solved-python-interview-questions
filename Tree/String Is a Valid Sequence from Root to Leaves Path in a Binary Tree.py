#Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#METHOD 1
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        arr="".join(map(str,arr))
        self.ans = [-1]
        def dfs(root,st=""):
            if not root :
                return
            st+=str(root.val)
            if st == arr and not root.left and not root.right:
                self.ans[0]=1
                return
            dfs(root.left,st)
            dfs(root.right,st)
        dfs(root)
        if self.ans[0]==1:
            return True
        return False

#METHOD 2
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        
        
        def dfs(root,pos,arr):
            if not root :
                return False
            if pos==len(arr):
                return False
            if root.val != arr[pos]:
                return False
            if not root.left and not root.right and pos==len(arr)-1:      # if not left and right and reached last pos of arr and arr[val]==node.val
                return True
            return (dfs(root.left,pos+1,arr) or dfs(root.right,pos+1,arr)) # either result from left path or right path
        
        pos = 0
        return dfs(root,pos,arr)
        
        

        
