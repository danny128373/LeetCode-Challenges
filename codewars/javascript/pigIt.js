function pigIt(str){
    newString = ''
    for (let i = 0; i < str.length; i++) {
        if (str[i] === ' ') {
            newString += str[i]
        }
    }
  }

console.log(pigIt('This is my string'))