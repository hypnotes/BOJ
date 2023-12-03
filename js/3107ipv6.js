const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let ipaddress = "";
const EIGHT = 8;

rl.on("line", function (line) {
  ipaddress = line;
  rl.close();
});

const handleTwoColons = (address) => {
  return address.split("::");
};

const padZero = (addr) => {
  return addr.padStart(4, "0");
};

rl.on("close", function () {
  let [left, right] = handleTwoColons(ipaddress);
  const finalL = [],
    finalR = [];
  if (left) left.split(":").forEach((addr) => finalL.push(padZero(addr)));
  if (right) right.split(":").forEach((addr) => finalR.push(padZero(addr)));
  const zeros = Array(EIGHT - (finalL.length + finalR.length)).fill("0000");
  let joined = finalL.concat(zeros, finalR);
  console.log(joined.map((v) => v).join(":"));
  process.exit();
});
