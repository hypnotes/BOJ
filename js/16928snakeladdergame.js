const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let ladderCount = 0;
let snakeCount = 0;
let counter = 0;
const ladders = Array(101).fill(0);
const snakes = Array(101).fill(0);
const game = Array(101).fill(0);

rl.on("line", function (line) {
  const first = parseInt(line.split(" ")[0]);
  const second = parseInt(line.split(" ")[1]);
  if (ladderCount === 0) {
    ladderCount = first;
    snakeCount = second;
  } else {
    if (counter !== ladderCount) {
      ladders[first] = second;
      counter++;
    } else snakes[first] = second;
  }
});

rl.on("close", function () {
  let queue = [1];

  while (queue.length) {
    const current = queue.shift();
    for (let i of [1, 2, 3, 4, 5, 6]) {
      let target = current + i;
      if (target > 100 || game[target]) continue;
      if (ladders[target]) target = ladders[target];
      else if (snakes[target]) target = snakes[target];
      if (game[target] === 0) {
        game[target] = game[current] + 1;
        queue.push(target);
      }
    }
  }
  console.log(game[100]);
});
