class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        n = len(points)
        points.sort()
        
        
        answer = 1
        
        killer = points[0]
        
        for i in range(1,n):
            
            kil_a,kil_b = killer
            a,b = points[i]
            
            if a<=kil_a<=b or a<=kil_b<=b or kil_a<=a<=kil_b or kil_a<=b<=kil_b:
                killer = [max(kil_a,a),min(kil_b,b)]
                continue
            else:
                killer =[a,b]
                answer+=1
        return answer