// var input = require("fs").readFileSync("/dev/stdin").toString().split(" ");
/** --------------------- INPUT --------------------- */
const path = require("path");

var input = require("fs")
  .readFileSync(path.resolve(__dirname, "input.txt"))
  .toString()
  .split("\n");

/** --------------------- GLOBAL --------------------- */

type Arr2D<T> = T[][];

const [rowCount, colCount, rotationCount] = input[0].split(" ").map(Number);

const arrays = input.slice(1, rowCount).map((row) => {
  return row.split(" ");
});

console.log("Your input is " + rowCount, colCount, rotationCount);
console.log("arrays: ", arrays);

/** --------------------- PURES --------------------- */
const getIterationCount = (colCount: number) => {
  return colCount / 2;
};

const iterate = (
  arrays: number[][],
  layer: number,
  rowCount: number,
  colCount: number
) => {
  let row: number;
  let col: number;
  const endCol = colCount - layer;
  const endRow = rowCount - layer;
  for (row = layer; row < endRow; row++) {
    for (col = layer; col < endCol; col++) {
      console.log("iam at ", arrays[row][col]);
    }
  }
};

const iterateAndCompress = (colCount: number) => {};

/** --------------------- EXECUTION --------------------- */
const ans = iterate(arrays, 0, rowCount, colCount);
console.log("✨: ", ans);
