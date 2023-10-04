class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
      
        if not root:
            return
        queue = deque()
        queue.append(root)
        queue.append(None)

        
        while len(queue)>1:
            
            n = len(queue)
            
            for i in range(n-1):
                    
                node = queue.popleft()
                node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            queue.popleft()
            queue.append(None)
        
        return root
                