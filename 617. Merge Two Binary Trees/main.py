# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Tree:
#     lis = []
#
#     def __init__(self):
#         self.root  = None
#
#     def add(self, x):
#         node = TreeNode(x)
#
#         if self.root is None:
#             self.root=node
#             Tree.lis.append(self.root)
#         else:
#             while True:
#                 point = Tree.lis[0]
#
#                 if point.left is None:
#                     point.left = node
#                     Tree.lis.append(point.left)
#                     return
#
#                 elif point.right is None:
#                     point.right = node
#                     Tree.lis.append(point.right)
#                     Tree.lis.pop(0)
#                     return


class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t2.right, t2.right)
        return t1
