const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  const nums = line.split(" ").map((num) => parseInt(num));
  nums.sort();
  const a = nums[0];
  const b = nums[1];
  let gcd = 1;
  let lcm = b;

  for (let i = 1; i < a+1; i++) {
    if (a % i === 0 && b % i === 0 && gcd < i) {
      gcd = i;
    }
  }
  let i = 1;
  while (true) {
    if ((a * i) % b === 0) {
      lcm = a * i;
      break;
    }
    i += 1;
  }
  console.log(gcd);
  console.log(lcm);

  rl.close();
});
