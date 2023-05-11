class Solution:
    def racecar(self, target: int) -> int:
            
        visited={(0,1)}
        queue = deque([(0, 1, 0)])

        while queue:

            pos,speed,level=queue.popleft()

            if pos==target:
                return level

            level+=1

            accelerate = (pos + speed, speed << 1)
            reverse = (pos, -1 if speed > 0 else 1)

            if accelerate not in visited:
                visited.add(accelerate)
                queue.append((accelerate[0],accelerate[1],level))

            if reverse not in visited:
                visited.add(reverse)    
                queue.append((reverse[0],reverse[1],level))
