/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    
    nums.map(el=>{
        init = fn(init,el)
    })
    
    return init
};