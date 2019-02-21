

from queue import Queue

def levelTraverse(root):
    if not root:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.val)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

