class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def traverse(root, soFar):
            if root is None:
                return
            if root.left is None and root.right is None:
                ans[0] += soFar * 10 + root.val
                return
            traverse(root.left, soFar * 10 + root.val)
            traverse(root.right, soFar * 10 + root.val)
        traverse(root, 0)
        return ans[0]