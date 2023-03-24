class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
                i=0
                while i<len(arr):
                    if arr[i]-1==i:
                        i+=1
                    else:
                        temp = arr[i]-1
                        if temp>len(arr)-1:
                            i+=1
                            continue
                        if arr[i] == arr[temp]:
                            i+=1
                            continue 
                        arr[i],arr[temp] = arr[temp], arr[i]
                res=[]
                for i in range(len(arr)):
        
                    if arr[i]!=i+1:
                        res.append(i+1)

                return res