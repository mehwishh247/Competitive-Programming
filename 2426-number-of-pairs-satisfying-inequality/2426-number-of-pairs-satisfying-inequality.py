class Solution:
    
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr=[]
        self.answer=0
        n=len(nums1)
        for i in range(n):
            arr.append(nums1[i]-nums2[i])    
        self.mergeSort(0,len(arr)-1,arr,diff)
        
       
        return self.answer

    def merge(self,arr1,arr2):
        i,j,k = 0,0,0
        arr=[0]*(len(arr1)+len(arr2))
        while i<len(arr1) and j<len(arr2):
            if arr1[i] <arr2[j]:
                arr[k] = arr1[i]
                i+=1
                k+=1
            else:
                arr[k] = arr2[j]
                j+=1
                k+=1

        while i<len(arr1):
                arr[k] = arr1[i]
                i+=1
                k+=1
        while j<len(arr2):
                arr[k] = arr2[j]
                j+=1
                k+=1

        return arr


    def mergeSort(self,left,right,arr,diff):
        if left==right:
            return [arr[left]]

        mid = left +(right-left)//2
        left_half  = self.mergeSort(left, mid, arr,diff) 
        right_half  = self.mergeSort(mid+1, right, arr,diff)

        for num in right_half:
            x =bisect_right(left_half,num+diff)
            self.answer+=x
        return self.merge(left_half, right_half)


    