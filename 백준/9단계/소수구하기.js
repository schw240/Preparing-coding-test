// 에라토스테네스의 체
// 소수를 구하면 그 소수의 배수는 소수가 될 수 없다.
// 그래서 그 배수들을 사전에 제거하고 남은 수를 이용해 소수를 구하는 법

// const fs = require('fs')
// const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(num => parseInt(num))


// const M = input[0]
// const N = input[1]

const M = 3
const N = 16

function isPrimeNum(num) {
    if (num < 2) {
        return false
    } else {
        for (let i = 2; i <= Number(Math.pow(i, 2)) + 1; i++) {
            if (num % i === 0) {
                return false
            }
        }
    }
    return ture
}

for (let i = M; i <= N; i++) {
    console.log(isPrimeNum(i))
    if (isPrimeNum(i) === true) {
        console.log(i)
    }
}