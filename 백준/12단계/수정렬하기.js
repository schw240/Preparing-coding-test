const fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const N = Number(input[0])
let nums = []

for (let i = 1; i <= N; i++) {
    nums.push(Number(input[i]))
}

nums = nums.sort((a, b) => a - b)

for (let num of nums) {
    console.log(num)
}