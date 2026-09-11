
# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: [int] = None, children: [list['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        que = deque()
        que.append(root)
        level = 0

        while que:
            size = len(que)
            level += 1
            for _ in range(size):
                cur = que.popleft()

                if cur.children is None:
                    continue

                for i in cur.children: 
                    que.append(i)
        
        return level

