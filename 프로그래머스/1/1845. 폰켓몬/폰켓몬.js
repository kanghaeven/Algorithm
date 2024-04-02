function solution(nums) {
    var answer = 0;
    const n = nums.length / 2;
    const set = new Set([...nums]).size;
    return n < set ? n : set;
}