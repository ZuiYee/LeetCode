# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS
# class Solution:
#     def searchBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
#         if root:
#             print(root.val)
#             # if root.val == val:
#             #     return root
#             if root.left:
#                 self.searchBST(root.left, root.val)
#             if root.right:
#                 self.searchBST(root.right, root.val)

# BFS
class Solution:
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

