# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

from pyparsing import Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:

        result = []

        que = deque()
        que.append(root)
        while que:
            size = len(que)
            value = 0
            for _ in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                value += cur.val
            result.append(value/size)

        return result
        

