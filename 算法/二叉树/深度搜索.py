def DFS(root):
    if root:
        print(root.val)
        DFS(root.left)
        DFS(root.right)