// const fs = require('fs')
// let input = fs.readFileSync('/dev/stdin').toString()

let N = 1000;

let cnt = 0;

for (let i = 1; i <= N; i++) {
    if (i < 100) {
        cnt += 1;
    }
    let arr = String(i)
    let A = Number(arr[0]) - Number(arr[1])
    let B = Number(arr[1]) - Number(arr[2])
    if (A == B) {
        cnt += 1;
    }                                   
}
                                        
console.log(cnt)