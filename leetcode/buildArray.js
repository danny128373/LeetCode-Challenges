/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function (target, n) {
  let counter = 0;
  let new_target = [];
  for (let i = target[0]; i <= target[target.length - 1]; i++) {
    counter += 1;
    new_target.push("Push");
    if (!target.includes(i)) {
      new_target.push("Pop");
    }
    if (n === counter) {
      return new_target;
    }
  }
  return new_target;
};

console.log(buildArray([1, 2, 4, 6], 4));
