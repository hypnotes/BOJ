const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let peopleNum = 0;
let partyNum = [];
let knows = -1;
let knowsTruth = [];
let parties = [];
// [attendNum, membesr[], flag]

rl.on("line", function (line) {
  let members = line.split(" ").map((v) => parseInt(v));
  if (peopleNum === 0) {
    peopleNum = members[0];
    partyNum = members[1];
    knowsTruth = Array(peopleNum).fill(0);
  } else if (knows === -1) {
    knows = members.shift();
    members.map((mem) => (knowsTruth[mem - 1] = 1));
  } else {
    parties.push([members.shift(), members], true);
  }
});

const bfs = (person) => {
  let needsCheck = [];
  parties.map(({ attendNum, members, flag }) => {
    if (flag) {
      if (members.includes(person)) {
        needsCheck += members;
      }
    }
  });
};

rl.on("close", function () {
  console.log(knowsTruth);
  console.log(parties);
});
