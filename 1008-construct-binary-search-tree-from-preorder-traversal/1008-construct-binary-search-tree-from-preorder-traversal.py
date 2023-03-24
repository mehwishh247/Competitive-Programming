# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, arr: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(arr[0])
        stack =[(root,arr[0])]
        
        for i in range(1,len(arr)):
            if arr[i]<stack[-1][0].val:
                newNode= TreeNode(arr[i])
                stack[-1][0].left = newNode 
                stack.append((newNode,arr[i]))
            else:
                temp = None
                while stack and stack[-1][0].val<arr[i]:
                    temp = stack.pop()
                newNode = TreeNode(arr[i])
                temp[0].right= newNode
                stack.append((newNode,arr[i]))

        return root