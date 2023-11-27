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
  let stack = [];
  let ans = [];
  for (let i = 0; i < inputCount; i++) {
    const [dir, num] = inputLines[i].split(" ");
    switch (dir) {
      case "1":
        stack.push(parseInt(num));
        break;
      case "2":
        ans.push(stack.pop() || -1);
        break;
      case "3":
        ans.push(stack.length);
        break;
      case "4":
        ans.push(stack.length ? 0 : 1);
        break;
      case "5":
        ans.push(stack.length ? stack[stack.length - 1] : -1);
        break;
    }
  }
  console.log(ans.join("\n"));
});
