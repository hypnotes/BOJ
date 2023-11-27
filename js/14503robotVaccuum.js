const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let rowMax = 0,
  colMax = 0;
let currentI = -1,
  currentJ = 0,
  currentDir = 0;
let roomMap = [];

// W,  N,  E,  S, -> N, E, S, W
const directtionX = [0, 0, 1, -1];
const directtionY = [1, -1, 0, 0];

let cleaned = 0;

rl.on("line", function (line) {
  const values = line.split(" ").map(Number);

  if (rowMax === 0) {
    [rowMax, colMax] = values;
  } else if (currentI === -1) {
    [currentI, currentJ, currentDir] = values;
  } else if (roomMap.length < rowMax) {
    roomMap.push(values);
  }
});

const checkOutOfBoard = (i, j) => {
  return i < 0 || j < 0 || i >= rowMax || j >= colMax;
};

const goBack = (i, j, dir) => {
  const newI = i - directtionY[dir];
  const newJ = j - directtionX[dir];

  if (checkOutOfBoard(newI, newJ)) return null;
  else return [newI, newJ];
};

const checkFourDirection = (i, j) => {
  let flag = 0;
  for (let d = 0; d < 4; d++) {
    const newI = i + directtionY[d];
    const newJ = j + directtionX[d];

    if (checkOutOfBoard(newI, newJ)) continue;
    const targetBoard = roomMap[newI][newJ];
    if (targetBoard !== 1 && targetBoard !== -1) flag = 1;
  }
  return flag;
};

rl.on("close", function () {
  while (true) {
    if (!roomMap[currentI][currentJ]) {
      roomMap[currentI][currentJ] = -1;
      cleaned++;
      console.log("cleaned: ", currentI, currentJ);
    }
    if (checkFourDirection(currentI, currentJ)) {
      const nextDir = 4 % (currentDir - 1);
      const newI = currentI + directtionY[nextDir];
      const newJ = currentJ + directtionX[nextDir];
      if (checkOutOfBoard(newI, newJ)) continue;
      currentI = newI;
      currentJ = newJ;
      currentDir = nextDir;
    } else {
      if (goBack() !== null) {
        const [a, b] = goBack();
        currentI = a;
        currentJ = b;
      } else {
        console.log(cleaned);
        return;
      }
    }
  }
});
