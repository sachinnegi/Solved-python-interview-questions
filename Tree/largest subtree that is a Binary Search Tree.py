#User function Template for python3

# Return the size of the largest sub-tree which is also a BST
class SubTree:
    def __init__(self):
        self.isBst = True
        self.rmin = float('inf')
        self.lmax = float('-inf')
        self.size = 0
        
def postorder(node):
    info = SubTree()
    if not node:
        return info
    left = postorder(node.left)
    right  = postorder(node.right)
    if ( left.lmax<node.data<right.rmin and left.isBst and right.isBst  ):
        info.size = left.size + right.size +1
        info.isBst = True
        info.rmin = min(node.data, left.rmin, right.rmin)
        info.lmax = max(node.data, left.lmax, right.lmax)
    else:
        info.isBst = False
        info.size = max(left.size, right.size)
    return info

def largestBst(root):
    info = postorder(root)
    return info.size

