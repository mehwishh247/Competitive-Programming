class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

            n = len(arr)
            i = n - 1
            while i > 0 and arr[i-1] <= arr[i]:
                i -= 1
            if i == 0:
                return arr
            i -= 1
            j = n - 1
            while j > i and arr[j] >= arr[i]:
                j -= 1
            while j > 0 and arr[j] == arr[j-1]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            return arr
