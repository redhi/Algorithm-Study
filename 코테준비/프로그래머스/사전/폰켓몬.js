function solution(nums) {
    var answer = 0;
    var dic =  {};
    for (let num of nums) {
        if (num in dic) {
            dic[num] = dic[num] + 1;
        }
        else {
            dic[num] = 1;
        }
    }
    n = parseInt(nums.length/2);
    
    if (n > Object.keys(dic).length) {
        return Object.keys(dic).length
    }
    return n;
}
let nums = [3,1,2,3]
console.log(solution(nums))