class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=nums
        

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right]+ sum(self.arr[left:right])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)