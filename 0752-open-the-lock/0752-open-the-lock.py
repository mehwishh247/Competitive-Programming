from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([('0000', 0)])
        visited = set(deadends)

        if '0000' in visited or target in visited:
            return -1
        visited.add('0000')

        while queue:
            node, level = queue.popleft()

            if node == target:
                return level

            for i in range(4):
                for d in (-1, 1):
                    kid = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                    if kid not in visited:
                        visited.add(kid)
                        queue.append((kid, level+1))

        return -1