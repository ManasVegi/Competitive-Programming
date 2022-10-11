class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, soFar):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1 if root.val >= soFar else 0
            res = 1 if root.val >= soFar else 0
            soFar = max(soFar, root.val)
            return res + helper(root.left, soFar) + helper(root.right, soFar)
        return helper(root, float('-inf'))