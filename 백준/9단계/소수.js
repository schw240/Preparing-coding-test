const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const M = Number(input[0])
const N = Number(input[1])
// const M = 64
// const N = 65

function isPrimeNum(num) {
    if (num < 2) {
        return false;
    }

    for (let i = 2; i < num; i++) {
        if (num % i == 0) {
            return false
        }
    }
    return true
}

let primes = []
let sum_value = 0
for (let i = M; i <= N; i++) {
    if (isPrimeNum(i) === true) {
        primes.push(i)
        sum_value += i
    }
}

if (!primes.length) {
    console.log(-1)
} else {
    console.log(sum_value)
    console.log(Math.min.apply(null, primes))
}