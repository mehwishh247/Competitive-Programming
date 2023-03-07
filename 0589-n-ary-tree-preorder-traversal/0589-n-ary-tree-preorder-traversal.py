"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def solut(node,arr):
            if node == None:
                return arr
            arr.append(node.val)
            for child in node.children:
                solut(child,arr)
            return arr
        
        return solut(root,[])
        