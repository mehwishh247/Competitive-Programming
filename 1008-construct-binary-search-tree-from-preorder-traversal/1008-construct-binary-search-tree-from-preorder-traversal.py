# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, arr: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(arr[0])
        stack =[root]
        
        for i in range(1,len(arr)):
            newNode = TreeNode(arr[i])
            if arr[i]<stack[-1].val:
                stack[-1].left = newNode 
            else:
                temp = None
                while stack and stack[-1].val<arr[i]:
                    temp = stack.pop()
                temp.right= newNode
            
            stack.append(newNode)

        return root