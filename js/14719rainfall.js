const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let WIDTH = 0,
  HEIGHT = 0;
let graph = [];
let rainfall = 0;

let stack = [];

rl.on("line", function (line) {
  if (WIDTH === 0) {
    [HEIGHT, WIDTH] = line.split(" ").map(Number);
  } else {
    graph = line.split(" ").map(Number);
  }
});

const emptyAndFindRain = (base) => {
  while (stack.length) {
    const popped = stack.pop();
    if (base > popped) rainfall += base - popped;
  }
  return;
};

const findInnerRain = (wall) => {
  const tempStack = stack.slice().sort((a, b) => a - b);
  if (wall <= tempStack[0]) return;
  for (let i = stack.length - 1; i >= 0; i--) {
    if (stack[i] < wall) {
      rainfall += wall - stack[i];
      stack[i] += wall - stack[i];
    } else return;
  }
};

rl.on("close", function () {
  let base = graph[0];

  for (let i = 1; i < WIDTH; i++) {
    const wall = graph[i];
    if (wall >= base) {
      emptyAndFindRain(base < wall ? base : wall);
      base = wall;
    } else if (i === WIDTH - 1) {
      findInnerRain(wall);
      emptyAndFindRain(base < wall ? base : wall);
    } else {
      findInnerRain(wall);
      stack.push(wall);
    }
  }
  console.log(rainfall);
});
