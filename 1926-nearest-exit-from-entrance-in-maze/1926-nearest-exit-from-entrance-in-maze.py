class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def isBorder(row,col):
            return row==0 or row==len(maze)-1 or col==0 or col==len(maze[0])-1
        
        def inBound(row,col):
            return 0<=row<len(maze) and 0<=col<len(maze[0])

        
        queue=deque([ (entrance,0) ])

        while queue:
            size=len(queue)

            for i in range(size):
                node,level=queue.popleft()
                curRow,curCol=node
                if (curRow!=entrance[0] or curCol!=entrance[-1]) and isBorder(curRow,curCol):
                    return level
                
                directions = [(curRow+1,curCol),(curRow-1,curCol),(curRow,curCol+1),(curRow,curCol-1)]

                for dr in directions:
                    if  inBound(dr[0],dr[1]) and maze[dr[0]][dr[-1]]==".":
                        maze[dr[0]][dr[-1]]="+"
                        queue.append(([dr[0],dr[-1]],level+1))
                
        return -1
