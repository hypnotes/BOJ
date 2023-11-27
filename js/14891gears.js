const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const TOTALGEARS = 4;
const CURRENT_LEFT = 6;
const CURRENT_RIGHT = 2;

let gears = [];
let rotation = 0;
let rotationMethod = [];

rl.on("line", function (line) {
  if (gears.length !== TOTALGEARS) {
    gears.push(line.split("").map(Number));
  } else if (!rotation) {
    rotation = Number(line);
  } else {
    rotationMethod.push(line.split(" ").map(Number));
  }
});

const rotate = (gearNumber, dir) => {
  if (dir === 1) {
    gears[gearNumber].unshift(gears[gearNumber].pop());
    return;
  }
  gears[gearNumber].push(gears[gearNumber].shift());
  return;
};
const getScore = () => {
  const scoreboard = [1, 2, 4, 8];
  let score = 0;
  gears.map((gear, idx) => {
    score += gear[0] * scoreboard[idx];
  });
  return score;
};

const rotateRightSide = (targetGear, targetDir) => {
  if (targetGear === TOTALGEARS) {
    return;
  }
  if (
    gears[targetGear][CURRENT_LEFT] === gears[targetGear - 1][CURRENT_RIGHT]
  ) {
    return;
  }

  rotateRightSide(targetGear + 1, targetDir * -1);
  rotate(targetGear, targetDir);
};

const rotateLeftSide = (targetGear, targetDir) => {
  if (targetGear === -1) {
    return;
  }
  if (
    gears[targetGear][CURRENT_RIGHT] === gears[targetGear + 1][CURRENT_LEFT]
  ) {
    return;
  }
  rotateLeftSide(targetGear - 1, targetDir * -1);
  rotate(targetGear, targetDir);
};

rl.on("close", function () {
  while (rotationMethod.length) {
    const [targetGear, targetDir] = rotationMethod.shift();
    rotateLeftSide(targetGear - 2, targetDir * -1);
    rotateRightSide(targetGear, targetDir * -1);
    rotate(targetGear - 1, targetDir);
  }

  console.log(getScore());
});
