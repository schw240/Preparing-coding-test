const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let N = input[0]

function factorial(n) {
    if (n < 2) {
        return 1
    }
    return n * factorial(n-1)
}

console.log(factorial(N))