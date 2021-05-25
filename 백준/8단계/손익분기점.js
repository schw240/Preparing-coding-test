const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().split(' ')

let A = Number(input[0])
let B = Number(input[1])
let C = Number(input[2])

let BEP = 0
if (C > B) {
    BEP = Math.floor(A / (C - B)) + 1
} else {
    BEP = -1
}

console.log(BEP)