/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function (s) {
  let power = 1,
    maxPowers = [];
  for (i = 0; i < s.length; i++) {
    if (s.charAt(i) === s.charAt(i + 1)) {
      power++;
    } else {
      maxPowers.push(power);
      power = 1;
    }
  }
  return Math.max(...maxPowers);
};

console.log(maxPower("leetcode"));
