function solution(s) {
    var answer = '';
    let len_s = s.length;
    if (len_s % 2 === 0){
        answer = s.substr(len_s/2 - 1, 2)
    } else if (len_s % 2 === 1) {
        answer = s.substr(len_s/2, 1)
    }
    return answer;
}