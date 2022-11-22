# Definition for a binary tree node.
from collections import deque
from typing import Optional
List = list
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root == None:
            return ans
        q = deque()
        q.append(root)
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
                if i == n - 1:
                    ans.append(v.val)
        return ans