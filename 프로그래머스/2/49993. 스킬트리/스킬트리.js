function solution(skill, skill_trees) {
    let answer = 0;
    skill_trees.forEach(t => {
        let s = skill.split("");
        const check = t.split("");
        let flag = true;
        for (let i = 0; i < check.length; i++) {
            if (s.includes(check[i])) {
                if (check[i] !== s.shift()) {
                    flag = false;
                    break;
                }
            }
        }
        if (flag === true) answer++;
    })
    return answer;
}

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "AQWER"])); // Output: 3
