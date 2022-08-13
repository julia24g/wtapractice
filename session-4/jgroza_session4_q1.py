from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSide(self, root):
        
        r = []
        if root is None:
            return r
        
        q = Queue()
        q.put(root)
        l = q.qsize()
        
        while l > 0:
            l = q.qsize()

            for i in range(l):
                c = q.get()
                if i == l - 1:
                    r.append(c.val)
                if c.left:
                    q.put(c.left)
                if c.right:
                    q.put(c.right)
        
        return r

# Test Case 1
tree = TreeNode(1)
tree.left = TreeNode(5)
tree.right = TreeNode(2)

sol = Solution()
print(sol.rightSide(tree))


# Test Case 2
tree2 = TreeNode(44)
tree2.left = TreeNode(9)
tree2.right = TreeNode(4)
tree2.left.left = TreeNode(52)
tree2.left.right = TreeNode(23)
            
sol2 = Solution()
print(sol2.rightSide(tree2))
        