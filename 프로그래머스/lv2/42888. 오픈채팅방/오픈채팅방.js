function solution(record) {
    let answer = [];
    let userMap = {};

    record.forEach(e => {
        const [action, userId, userName] = e.split(' ');

        switch (action) {
            case 'Enter':
                userMap[userId] = userName; // 사용자 정보 최신화
                answer.push({ action: 'enter', userId }); // 동작과 id 저장
                break;
            case 'Leave':
                answer.push({ action: 'leave', userId });
                break;
            case 'Change':
                userMap[userId] = userName;
                break;
        }
    });

    answer = answer.map(action => {
        const userName = userMap[action.userId]; // 사용자 이름
        if (action.action === 'enter') {
            return `${userName}님이 들어왔습니다.`;
        } else {
            return `${userName}님이 나갔습니다.`;
        }
    });

    return answer;
}
