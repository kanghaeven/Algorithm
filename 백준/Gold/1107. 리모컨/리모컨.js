const fs = require('fs');

// 입력 받기
const [channelN, M, ...brokenButtons] = fs.readFileSync('/dev/stdin').toString().trim().split(/\s/).map(Number);

// 고장나지 않은 버튼 배열 생성
const buttons = [];
for (let b = 0; b < 10; b++) {
  if (brokenButtons.indexOf(b) === -1) buttons.push(b);
}

// 채널 이동에 필요한 최소 버튼 누름 횟수 계산하는 함수
function pressButtons(channel) {
  const channelDigits = String(channel).split('').map(Number);

  // 해당 숫자를 누르는데 필요한 버튼 횟수를 반환
  function pressSingleDigit(digit) {
    return Math.abs(digit - channelDigits[0]);
  }

  // 채널을 이동하는데 필요한 버튼 횟수 계산
  let minPressCount = Math.abs(channel - 100); // 초기값은 100번에서 +, -만을 이용해 이동하는 경우
  for (let i = 0; i <= 1000000; i++) {
    const canUse = String(i).split('').every(digit => buttons.includes(Number(digit)));
    if (canUse) {
      const pressCount = Math.abs(channel - i) + String(i).length;
      minPressCount = Math.min(minPressCount, pressCount);
    }
  }

  return minPressCount;
}

// 최소 버튼 누름 횟수 계산
const minPress = Math.min(
  Math.abs(channelN - 100), // +, - 버튼만을 사용하는 경우
  pressButtons(channelN)    // 숫자 버튼을 사용하는 경우
);

console.log(minPress);
