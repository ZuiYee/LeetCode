def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
    if root:
        q = []
        q.append(root)

        while q:
            n = q.pop(0)
            if n.val == val:
                return n
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(root.right)
    else:
        return None