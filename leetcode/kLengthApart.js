var kLengthApart = function (nums, k) {
  const start = nums.findIndex((x) => x === 1);
  if (start === -1) {
    return true;
  }
  let prev = start;
  for (let i = start + 1; i < nums.length; i++) {
    if (nums[i] === 1) {
      if (i - prev <= k) {
        return false;
      }
      prev = i;
    }
  }
  return true;
};

console.log(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2));
