function solution(string) {
    let newString = ''
    for (let i = 0; i < string.length; i++) {
      if (string[i] === string[i].toLowerCase()) {
        newString += string[i]
      } else {
        newString += ' ' + string[i]
      }
    }
    return newString
}

console.log(solution("howAreYou"))