// const fs = require('fs')
// let input = fs.readFileSync('/dev/stdin').toString().split('\n')

// let inputs = []
// inputs = input[0].split(' ')

const N = 10
const X = 5

let numbers = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]

let res = ''
for (let i = 0; i < N; i++) {
    if (numbers[i] < X) {
        res += numbers[i] + ' '
    }
}

console.log(res)