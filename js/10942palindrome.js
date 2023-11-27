const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = 0;
let arr = [-1];
let m = 0;
let testcases = [];

let palindrome = Array.from({ length: 2001 }, () => Array(2001).fill(0));

const maxRecursionDepth = 1000;
const isPalindrome = (i, j, depth) => {
  if (depth > maxRecursionDepth) return 0;
  if (i === j) {
    palindrome[i][j] = 1;
    return 1;
  }
  if (j - i === 1 && arr[i] === arr[j]) {
    palindrome[i][j] = 1;
    return 1;
  }
  if (arr[i] === arr[j] && isPalindrome(i + 1, j - 1, depth+1)) {
    palindrome[i][j] = 1;
    return 1;
  }

  return 0;
};

rl.on("line", function (line) {
  if (n === 0) n = parseInt(line);
  else if (m === 0 && arr.length === 0)
    arr.push(line.split(" ").map((v) => parseInt(v)));
  else if (testcases.length === 0 && m === 0) m = parseInt(line);
  else {
    testcases.push(line.split(" ").map((v) => parseInt(v)));
  }
});

rl.on("close", function () {
  testcases.map((pair) => {
    console.log(isPalindrome(pair[0], pair[1], 1));
  });
});
