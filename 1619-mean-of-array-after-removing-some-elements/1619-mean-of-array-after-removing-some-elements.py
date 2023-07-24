class Solution:
    def trimMean(self, arr: List[int]) -> float:
        def quickSelect(arr, start, end, k):
            pivot = arr[end]
            left = start

            for right in range(start, end):
                if arr[right] <= pivot:
                    arr[right], arr[left] = arr[left], arr[right]
                    left += 1

            arr[left], arr[end] = arr[end], arr[left]

            if left > k: return quickSelect(arr, start, left-1, k)
            elif left < k: return quickSelect(arr, left + 1, end, k)
            else: return arr[left]

        n = len(arr)
        k = n // 20
        quickSelect(arr, 0, len(arr) - 1, k)
        quickSelect(arr, k, n-1, n-k)

        return mean(arr[k:-k])
