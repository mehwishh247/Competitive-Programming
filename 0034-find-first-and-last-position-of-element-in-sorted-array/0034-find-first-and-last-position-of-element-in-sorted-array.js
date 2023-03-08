/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    occurance = (arr, target,first) => {
    let low = 0
    let high = arr.length - 1
    
    while (low <= high) {
        mid = low + Math.floor((high - low) / 2)
        
        if (target < arr[mid]) {
            high = mid - 1
        }
        else if (target > arr[mid]) {
            low = mid + 1
        }
        else {
            if (target != arr[mid - 1] && target != arr[mid + 1]) {
                return mid
             }
            if (target == arr[first ? mid-1: mid+1]) {
                first ? high = mid - 1 : low = mid + 1

            }
            else {
                return mid
            }
        }


    }
    return -1
} 

    let result = [occurance(nums,target,true),occurance(nums,target,false)]
    
    return result
    
};