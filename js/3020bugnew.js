const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");
const [n, h] = input
  .shift()
  .split(" ")
  .map((v) => parseInt(v));

//종유석
const bottomArr = Array.from({ length: h + 1 }, () => 0);
//석순
const topArr = Array.from({ length: h + 1 }, () => 0);

input.forEach((v, idx) => {
  idx % 2 === 0 ? bottomArr.push(v) : topArr.push(v);
});

const binarySearch = (arr, finding, i, j) => {
  if (j - i <= 0) {
    return -1;
  }
  const midIdx = parseInt(i + (j - i) / 2);
  if (arr[midIdx] < finding) {
    const rightResult = binarySearch(arr, finding, midIdx + 1, j);
    return rightResult !== -1 ? rightResult : midIdx;
  } else {
    return binarySearch(arr, finding, i, midIdx);
  }
};

console.log(topArr, bottomArr)
topArr.sort();
bottomArr.sort();
let ans = Infinity;
let ansCount = 0;
for (let i = 1; i < h + 1; i++) {
  const topBreak = n / 2 - 1 - binarySearch(topArr, h - i + 1, 0, n / 2);
  const bottomBreak = n / 2 - 1 - binarySearch(bottomArr, i, 0, n / 2);
  const totalBreak = topBreak + bottomBreak;
  if (totalBreak < ans) {
    ans = totalBreak;
    ansCount = 1;
  } else if (totalBreak === ans) ansCount++;
}
console.log(ans, ansCount);
