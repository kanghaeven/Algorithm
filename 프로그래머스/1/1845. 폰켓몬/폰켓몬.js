function solution(nums) {
    var answer = 0;
    const n = nums.length / 2;
    const set = new Set([...nums]);
    const setn = [...set].length;
    return n < setn ? n : setn;
}