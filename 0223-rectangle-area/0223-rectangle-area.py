class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        xleft=max(ax1,bx1)
        xright=min(ax2,bx2)
        
        ybotm=max(ay1,by1)
        ytop=min(ay2,by2)
        
        dx=xright-xleft
        dy=ytop-ybotm
        comm=0
        
        if dx>0 and dy>0:
            comm=dx*dy
        a=abs(ax2-ax1)*abs(ay2-ay1)
        b=abs(bx2-bx1)*abs(by2-by1)
        
        area=a+b-comm
        
        return area