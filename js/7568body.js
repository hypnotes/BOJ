const readline = require("readline");

function solution(input) {
  const order = input.slice();
  order.sort(function (a, b) {
    if (b[0] === a[0]) {
      return b[1] - a[1];
    }
    return b[0] - a[0];
  });

  for (let i = 0; i < order.length; i++) {
    for ( let j = i-1; j >= 0; j--){
      if(order[i][0]<order[j][0] && order[j])
    }
  }
  console.log(order)
  order.sort((a, b) => a[3] - b[3]);
  const ans = order.map((element) => element[2]);
  console.log(ans.join(" "));
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputCount = 0;
let list = [];

rl.on("line", function (line) {
  if (inputCount === 0) {
    inputCount = parseInt(line);
  } else {
    const values = line.split(" ").map((v) => parseInt(v));
    if (list.length === 0) {
      values.push(0, 0);
    } else {
      values.push(0);
      values.push(list.length);
    }
    list.push(values);
    if (list.length === inputCount) {
      solution(list);
      rl.close();
    }
  }
});
