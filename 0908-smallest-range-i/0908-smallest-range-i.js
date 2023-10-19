/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    let max=0,min=10000;
    nums.forEach((val)=>{
        if(val>=max){
            max=val;
        }
        if(val<=min){
            min=val;
        }
    });
    if(max-min>2*k)
    return max-min-2*k;
    else 
    return 0
};