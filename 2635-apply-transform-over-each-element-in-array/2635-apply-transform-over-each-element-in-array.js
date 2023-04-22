/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    arr.map((el,id)=>{
        arr[id]=fn(el,id)
    })
    return arr
};