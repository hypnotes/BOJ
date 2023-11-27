const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let rowMax = 0,
  colMax = 0;
let farmland = [];
let visited = [];
let answer = 0;
let isPeak = true;

// W, NW, N, NE, E, SE, S, SW
const directions = [
  [0, -1],
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, 1],
  [1, 1],
  [1, 0],
  [1, -1],
];

const dy = [-1, 0, 1, 0, 1, 1, -1, -1];
const dx = [0, 1, 0, -1, 1, -1, -1, 1];

rl.on("line", function (line) {
  if (rowMax === 0) {
    const [a, b] = line.split(" ").map((v) => parseInt(v));
    rowMax = a;
    colMax = b;
    visited = Array.from({ length: rowMax }, () => Array(colMax).fill(false));
  } else {
    farmland.push(line.split(" ").map(Number));
  }
});

function dfs(y, x) {
  visited[y][x] = 1;
  for (let i = 0; i < 8; i++) {
    let ny = y + dy[i];
    let nx = x + dx[i];
    if (ny < 0 || nx < 0 || ny >= rowMax || nx >= colMax) {
      continue;
    }
    if (farmland[ny][nx] > farmland[y][x]) {
      isPeak = 0;
    }
    if (farmland[ny][nx] === farmland[y][x] && !visited[ny][nx]) {
      dfs(ny, nx);
    }
  }
}

rl.on("close", function () {
  farmland.map((row, rowIdx) => {
    row.map((_, colIdx) => {
      if (!visited[rowIdx][colIdx]) {
        isPeak = true;
        dfs(rowIdx, colIdx);
        if (isPeak) {
          answer += 1;
        }
      }
    });
  });

  console.log(answer);
});
