# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def helper(node, level, position, levels):
            if not node:
                return
            if level not in levels:
                levels[level] = []
            levels[level].append((position, node.val))
            helper(node.left, level + 1, position * 2, levels)
            helper(node.right, level + 1, position * 2 + 1, levels)

        levels = {}
        helper(root, 0, 0, levels)

        max_width = 0
        for level in levels:
            nodes = levels[level]
            width = nodes[-1][0] - nodes[0][0] + 1
            max_width = max(max_width, width)

        return max_width

