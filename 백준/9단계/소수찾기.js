const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const nums = input[1].split(' ').map(Number)
let cnt = 0

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

for (let num of nums) {
    if (isPrimeNum(num) === true) {
        cnt += 1
    }
}

console.log(cnt)