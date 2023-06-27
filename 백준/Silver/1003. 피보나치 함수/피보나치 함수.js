const fs = require('fs');
const [T, ...N] = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

for (let i = 0; i < T; i++) {
	const num = N[i];
	const fibonacci = [[1, 0], [0, 1]];

	for (let j = 2; j <= num; j++) {
		fibonacci[j] = [
			fibonacci[j - 1][0] + fibonacci[j-2][0],
			fibonacci[j - 1][1] + fibonacci[j-2][1]
		];
	};
	console.log(fibonacci[num].join(" "));
};
