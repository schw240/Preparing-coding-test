function solution(a, b) {
    var answer = '';
    const days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    const months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let sum = 0;
    for (let i = 0; i < a-1; i++){
        sum += months[i];
    }
    sum += b;
    answer = days[sum % 7]
    return answer;
}