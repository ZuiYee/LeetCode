"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        if root:
            lis = []
            lis.append(root.val)
            if root.children:
                for child in root.children:
                    lis.extend(self.preorder(child))
        return lis