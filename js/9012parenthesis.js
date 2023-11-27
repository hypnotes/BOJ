const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputCount = 0;
let inputLines = [];

rl.on("line", function (line) {
  if (inputCount === 0) {
    inputCount = parseInt(line);
  } else {
    inputLines.push(line);
  }
});


rl.on("close", function () {
  let deque = [];
  let ans = [];
  for (let i = 0; i < inputCount; i++) {
    const [dir, num] = inputLines[i].split(" ");
    switch (dir) {
      case "size":
        ans.push(deque.length);
        break;
      case "empty":
        ans.push(deque.length ? 0 : 1);
        break;
      case "front":
        ans.push(deque[0] || -1);
        break;
      case "back":
        ans.push(deque[deque.length - 1] || -1);
        break;
      case "push_front":
        deque.unshift(num);
        break;
      case "push_back":
        deque.push(num);
        break;
      case "pop_front":
        ans.push(deque.shift() || -1);
        break;
      case "pop_back":
        ans.push(deque.pop() || -1);
    }
  }
  console.log(ans.join("\n"));
});
