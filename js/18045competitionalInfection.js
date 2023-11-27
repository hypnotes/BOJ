const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let rowMax = 0,
  colMax = 0;
let testGrid = [];
let goalSecond, goalX, goalY;
let needsSpread = [[]];

// W,  N,  E,  S,
const directtionX = [-1, 0, 1, 0];
const directtionY = [0, 1, 0, -1];

rl.on("line", function (line) {
  if (rowMax === 0) {
    const [a, b] = line.split(" ").map(Number);
    rowMax = a;
    colMax = b;
  } else if (testGrid.length !== rowMax) {
    testGrid.push(line.split(" ").map(Number));
  } else {
    const [s, x, y] = line.split(" ").map(Number);
    goalSecond = s;
    goalX = x;
    goalY = y;
  }
});

const infect = (i, j) => {
  for (let d = 0; d < 4; d++) {
    const newI = i + directtionY[d];
    const newJ = j + directtionX[d];
    if (newI < 0 || newI >= rowMax || newJ < 0 || newJ >= colMax) continue;
    if (testGrid[newI][newJ]) continue;
    testGrid[newI][newJ] = testGrid[i][j];
    needsSpread.push([testGrid[i][j], newI, newJ]);
  }
};

const sortNeedsSpread = () => {
  needsSpread.sort((a, b) => a[0] - b[0]);
};

rl.on("close", function () {
  let currentSecond = 0;

  for (let i = 0; i < rowMax; i++) {
    for (let j = 0; j < colMax; j++) {
      if (testGrid[i][j]) needsSpread.push([testGrid[i][j], i, j]);
    }
  }

  sortNeedsSpread();
  needsSpread.push([]);

  while (currentSecond < goalSecond) {
    needsSpread.shift()
    while (needsSpread.length && needsSpread[0].length) {
      const [_virusType, ci, cj] = needsSpread.shift();
      infect(ci, cj);
    }
    sortNeedsSpread();
    needsSpread.push([]);
    currentSecond++;
  }
  console.log(testGrid[goalX - 1][goalY - 1]);
});
