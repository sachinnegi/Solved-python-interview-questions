class Codec:
    def serialize(self, root):
        if not root:
            return ""
        que = deque([root])
        st = []
        while que:
            node = que.popleft()
            if node:
                st.append(str(node.val))
                que.append(node.left)    
                que.append(node.right)
            else:
                st.append('#')
        return ','.join(st)
                
    
    def deserialize (self, data):
        if not data: return None
        nodes = data.split(',')
        nodes = [int(i) if i!="#" else None for i in nodes ]
        # print(nodes)
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 0
        while q:
            node = q.popleft()
            if nodes[index+1]!=None:
                node.left = TreeNode(int(nodes[index+1]))
                q.append(node.left)
        
            if nodes[index+2]!=None:
                node.right = TreeNode(int(nodes[index+2]))
                q.append(node.right)
            index += 2
        return root
