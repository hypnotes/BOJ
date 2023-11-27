const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (line) {
  const roomNumber = Array.from(line);
  let maxSet = 0;
  let numberDictionary = Array.from({ length: 9 }, () => 0);
  let numCount = 0;
  roomNumber.map((char) => {
    if (char === "9" || char === "6") {
      numberDictionary[6] += 1;
      numCount = Math.ceil(numberDictionary[6] / 2);
    } else {
      numberDictionary[parseInt(char)] += 1;
      numCount = numberDictionary[parseInt(char)];
    }
    if (numCount > maxSet) {
      maxSet = numCount;
    }
  });
  console.log(maxSet);
  rl.close();
});
