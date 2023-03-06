t = int(input())

for i in range(t):
 n, k = map(int, input().split(" "))
 grid = []
 for j in range(n):
  grid.append(list(map(int, input().split())))

 from collections import defaultdict
 
 
 cntR = defaultdict(int)
 cntL = defaultdict(int)
  
 for row in range(len(grid)):
     x=[0]
     x.extend(grid[row])
     x.append(0)
     grid[row]=x
     
 
 initialRow =[ [0]*(len(grid[0]))]
 initialRow.extend(grid)
 initialRow.append( [0]*(len(grid[0])))
 
 curMax = 0 
 
 grid=initialRow
 for row in range(len(grid)):
     for col in range(len(grid[0])):
         cntR[row-col] += grid[row][col]
         cntL[row+col] += grid[row][col]
         
         
 
 for row in range(1,len(grid)-1):
     for col in range(1,len(grid[0])-1):
         curMax = max(curMax,cntR[row-col]+cntL[row+col]-grid[row][col]) 
    
 print(curMax)
  
