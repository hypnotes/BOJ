const readline = require("readline");
// TODO
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputCount = 0;
let m = 0;
let n = 0;
let matrix = [];
let testcaseNum = 0;
let testcases = [];

rl.on("line", function (line) {
  if (inputCount === 0) {
    const matrixSize = line.split(" ").map((v) => parseInt(v));
    n = matrixSize[0];
    m = matrixSize[1];
  } else if (inputCount > 0 && inputCount < n + 1) {
    matrix.push(line.split(" ").map((v) => parseInt(v)));
  } else if (inputCount === 1 + n) {
    testcaseNum = parseInt(line);
  } else {
    testcases.push(line.split(" ").map((v) => parseInt(v)));
  }
  inputCount += 1;
});

rl.on("close", function () {
  let ans = [];
  let prev = 0;
  for (let i = 0; i < n; i++) {
    let s = 0;
    let r = 
    for (let j = 0; j < m; j++) {
      matrix[i][j] = prev + matrix[i][j];
      prev = matrix[i][j];
    }
  }
  console.log(matrix);
  for (let i = 0; i < testcaseNum; i++) {
    const [a, b, c, d] = testcases[i];
    let s = 0;
    for (let j = a - 1; j < c; j++) {
      s += matrix[i][d] - matrix[i][b - 1];
      ans.push(s);
    }
  }
  console.log(ans.join("\n"));
});
