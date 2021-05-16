const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = [];

rl.on('line', function(line) {
    input.push(line)
}).on('close', function() {
    while(input[i].split(' ')[0] !== 0 && input[i].split(' ')[1]) {
        console.log(input[i].split(' ')[0] + input[i].split(' ')[1])
    }
    process.exit()
})``