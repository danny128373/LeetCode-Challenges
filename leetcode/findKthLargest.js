/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  return nums
    .sort(function (a, b) {
      return a - b;
    })
    .reverse()[k - 1];
};
