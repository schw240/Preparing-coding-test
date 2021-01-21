function solution(answers) {
    var answer = [];
    var cnt1 = 0
    var cnt2 = 0
    var cnt3 = 0
    const ans1 = [1,2,3,4,5]
    const ans2 = [2,1,2,3,2,4,2,5]
    const ans3 = [3,3,1,1,2,2,4,4,5,5]
    
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === ans1[i%ans1.length]) cnt1 += 1
        if (answers[i] === ans2[i%ans2.length]) cnt2 += 1
        if (answers[i] === ans3[i%ans3.length]) cnt3 += 1
    }
    
    const tmp = [cnt1, cnt2, cnt3]
    var max = 0
    
    for (let i = 0; i < tmp.length; i++) {
        if (Math.max.apply(null, tmp) === tmp[i]){
            answer.push(i+1)
        }
        
    }
    
    return answer;
}