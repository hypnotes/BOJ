const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = 0;
let arr = Array.from({ length: 101 }).fill(0);
let visited = Array.from({ length: 101 }).fill(false);
let arrIdx = 1;

const dfs = (startIdx, goalValue) => {
  if (arr[startIdx] === goalValue) {
    visited[startIdx] = true;
    return true;
  } else {
    if (!visited[startIdx]) {
      visited[startIdx] = true;
      if (dfs(arr[startIdx], goalValue)) return true;
      else {
        visited[startIdx] = false;
        return false;
      }
    } else return false;
  }
};

rl.on("line", function (line) {
  if (n === 0) n = parseInt(line);
  else {
    arr[arrIdx] = parseInt(line);
    arrIdx++;
  }
});

rl.on("close", function () {
  for (let i = 1; i <= n; i++) {
    dfs(i, i);
  }

  const trueVals = visited.reduce((list, currentVal, currentIdx) => {
    if (currentVal) {
      list.push(arr[currentIdx]);
    }
    return list;
  }, []);

  console.log(trueVals.length);
  console.log(trueVals.sort().join("\n"));
});
