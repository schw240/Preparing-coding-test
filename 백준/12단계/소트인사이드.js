const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('')

console.log(input.sort((a, b) => b - a).join(''))
