
# METHOD-1

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = collections.deque()
        stack = []
        node = root
        while stack or node:
            while node:
                result.appendleft(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        return result


# METHOD-2

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = collections.deque()
        stack = [root]
        while stack :
            node = stack.pop()
            result.appendleft(node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

        