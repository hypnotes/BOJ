const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});a

let inputCount = 0;
let aSize = [];
let bSize = [];
let matrixA = [];
let matrixB = [];

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
    for (let j = 0; j < m; j++) {
      matrix[i][j] = prev + matrix[i][j];
      prev = matrix[i][j];
    }
  }
  console.log(matrix);
  for (let i = 0; i < testcaseNum; i++) {
    const [a, b, c, d] = testcases[i];
    let abPrev = 0;
    if (a === 1 && b === 1) {
      abPrev = 0;
    } else if (b === 1) {
      abPrev = matrix[a - 2][m - 1];
    } else {
      abPrev = matrix[a - 1][b - 2];
    }
    ans.push(matrix[c - 1][d - 1] - abPrev);
    console.log(ans);
  }
  console.log(ans.join("\n"));
});
