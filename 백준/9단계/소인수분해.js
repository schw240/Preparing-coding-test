const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

let N = Number(input[0])
// len N = 72

let i = 2;
while (N != 1) {
    if (N % i === 0) {
        console.log(i)
        N = N / i
    } else {
        i += 1
    }
}