def BTtoDll(root):
    if root ==None:
        return root
    if root.left:
        left = BTtoDll(root.left) # traverse to the leftmost subtree
        while left.right:
            left = left.right       # find the inorder predecssor of current root

        left.right = root           #connect predecessor's right to root
        root.left = left            # connect root's left to predecessor

    if root.right:
        right = BTtoDll(root.right) # traverse to right subtree
        while right.left:
            right  = right.left     # find inorder successor of root

        root.right = right
        right.left = root
    return root

def returnHead(root):
    head = BTtoDll(root)
    if not head:
        return None
    while head.left:            # find the pointer to the head of the link list since some node which is not head was returned
        head = head.left
    return head
    
        
