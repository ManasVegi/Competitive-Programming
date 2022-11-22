# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = -1
        def helper(root):
            if root == None:
                return
            if root.left == None and root.right == None:
                self.count += 1
                if self.count == k:
                    self.ans = root.val
                return
            helper(root.left)
            self.count += 1
            if self.count == k:
                self.ans = root.val
            if self.count >= k:
                return
            helper(root.right)
        helper(root)
        return self.ans