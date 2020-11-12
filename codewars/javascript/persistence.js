function persistence(num) {
  //set multiplyCount equal 0
  //turn the number into an array of nums
  //while the length of the array is more than 1
  //multiply each digit together
  //the product becomes the new arr
  //return multiplyCount

  var arr = num.toString().split("");
  var multiplyCount = 0;
  var product;
  while (arr.length > 1) {
    product = arr.reduce(function (a, b) {
      return a * b;
    });
    multiplyCount++;
    arr = product.toString().split("");
  }
  return multiplyCount;
}

console.log(persistence(39)); // 3
console.log(persistence(999)); // 4
console.log(persistence(4)); // 0
