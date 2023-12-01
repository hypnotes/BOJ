const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  rl.close();
});

rl.on("close", function () {
  const date = new Date();
  console.log(date.getFullYear());
  console.log(date.getMonth() + 1);
  console.log(date.getDate());
  process.exit();
});
