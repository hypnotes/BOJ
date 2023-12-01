const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let rowLength = 0;
let colLength = 0;
let rotateCount = 0;

let givenArray = [];

rl.on("line", function (line) {
  if (rowLength === 0) {
    [rowLength, colLength, rotateCount] = line.split(" ").map(Number);
    newArray = Array.from({ length: rowLength }, () =>
      Array.from({ length: colLength }, () => 0)
    );
  } else {
    givenArray.push(line.split(" ").map(Number));
    if (givenArray.length === rowLength) {
      rl.close();
    }
  }
});

const flatten = (loop) => {
  let flattenedArr = [];

  for (let j = loop; j < colLength - loop; j++) {
    flattenedArr.push(givenArray[loop][j]);
  }
  flattenedArr.pop();
  for (let i = loop; i < rowLength - loop; i++) {
    flattenedArr.push(givenArray[i][colLength - loop - 1]);
  }
  flattenedArr.pop();

  for (let j = colLength - loop - 1; j >= loop; j--) {
    flattenedArr.push(givenArray[rowLength - loop - 1][j]);
  }
  flattenedArr.pop();

  for (let i = rowLength - loop - 1; i >= loop; i--) {
    flattenedArr.push(givenArray[i][loop]);
  }
  flattenedArr.pop();
  return flattenedArr;
};

const rotate = (rotateArr) => {
  const effectiveRotateCount = rotateCount % rotateArr.length;
  return rotateArr.slice(effectiveRotateCount).concat(rotateArr.slice(0, effectiveRotateCount));
};
const copyRotatedArr = (arr, loop) => {
  let a = 0;

  for (let j = loop; j < colLength - loop; j++) {
    givenArray[loop][j] = arr[a];
    if (j < colLength - loop - 1) a++;
  }
  for (let i = loop; i < rowLength - loop; i++) {
    givenArray[i][colLength - loop - 1] = arr[a];
    if (i < rowLength - loop - 1) a++;
  }
  for (let j = colLength - loop - 1; j >= loop; j--) {
    givenArray[rowLength - loop - 1][j] = arr[a];
    if (j > loop) a++;
  }
  for (let i = rowLength - loop - 1; i > loop; i--) {
    givenArray[i][loop] = arr[a];
    a++;
  }
};

rl.on("close", function () {
  for (let loop = 0; loop < Math.min(rowLength, colLength) / 2; loop++) {
    const arr = flatten(loop);
    const rotatedArr = rotate(arr);
    copyRotatedArr(rotatedArr, loop);
  }
  console.log(givenArray.map((row) => row.join(" ")).join("\n"));

  process.exit();
});
