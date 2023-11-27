const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let memberCount = 0;
let friendRelationships = [];

rl.on("line", function (line) {
  const [first, second] = line.split(" ").map(Number);

  if (first === -1 && second === -1) {
    rl.close();
  }
  if (memberCount === 0) {
    memberCount = first;
    friendRelationships = Array.from({ length: memberCount + 1 }, () =>
      Array(memberCount + 1).fill(null)
    );
  } else {
    friendRelationships[first][second] = 1;
    friendRelationships[second][first] = 1;
  }
});

rl.on("close", function () {
  console.log(friendRelationships);

  // i, j != 0 , i!==j
  for (let i = 1; i < memberCount + 1; i++) {
    let thisLine = [];
    for (let j = 1; j < i; j++) {
      
    }
  }
});
