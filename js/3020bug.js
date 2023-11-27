const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = 0;
let h = 0;
let counter = 0;
let topArr = [];
let bottomArr = [];

const binarySearch = (arr, finding, left, right) => {
  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] >= finding) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return arr.length - right;
};

rl.on("line", function (line) {
  if (n === 0) {
    n = parseInt(line.split(" ")[0]);
    h = parseInt(line.split(" ")[1]);
  } else {
    if (counter % 2) topArr.push(parseInt(line));
    else bottomArr.push(parseInt(line));
    counter++;
  }
});

rl.on("close", function () {
  topArr.sort();
  bottomArr.sort();
  let ans = n;
  let ansCount = 0;
  for (let i = 1; i < h+1; i++) {
    const topBreak = binarySearch(topArr, h - i + 1, 0, n / 2);
    const bottomBreak = binarySearch(bottomArr, i, 0, n / 2);

    const totalBreak = topBreak + bottomBreak;
    if (totalBreak === ans) {
      ansCount++;
      continue
    } 
    if(ans > totalBreak){
      ans = totalBreak;
      ansCount=1
    }
  }
  console.log(ans, ansCount);
});
