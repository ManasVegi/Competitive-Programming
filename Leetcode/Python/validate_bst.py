class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, minval, maxval):
            if root is None:
                return True
            return  (root.val < maxval and root.val > minval) \
                and helper(root.left, minval, root.val) \
                and helper(root.right, root.val, maxval)
        return helper(root, float('-inf'), float('inf'))