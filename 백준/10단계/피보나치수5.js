const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

let n = input[0]

function fibo(n) {
    if (n < 2) {
        return n
    }
    if (n == 2) {
        return 1
    }
    return fibo(n - 1) + fibo(n - 2)
}

console.log(fibo(n))