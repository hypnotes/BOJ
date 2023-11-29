const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let numberGoal = 0;
let findIndexOf = 0;

rl.on("line", function (line) {
  [numberGoal, findIndexOf] = line.split(" ").map(Number);
  rl.close();
});

const connectNumbers = (number, goal) => {
  let untilNow = 0;
  for (let num = 1; num <= number; num++) {
    untilNow += num.toString().length;
    if (untilNow >= goal) {
      const numString = num.toString();
      return numString[numString.length - (untilNow - goal) - 1];
    }
  }
  return -1;
};

rl.on("close", function () {
  const answer = connectNumbers(numberGoal, findIndexOf);
  console.log(answer);
  process.exit();
});
