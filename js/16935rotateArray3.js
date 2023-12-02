const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let rowLength = 0;
let colLength = 0;
let calcCount = 0;
let calcCommand = [];

let givenArray = [];

rl.on("line", function (line) {
  if (rowLength === 0) {
    [rowLength, colLength, calcCount] = line.split(" ").map(Number);
    newArray = Array.from({ length: rowLength }, () =>
      Array.from({ length: colLength }, () => 0)
    );
  } else if (givenArray.length !== rowLength) {
    givenArray.push(line.split(" ").map(Number));
  } else {
    calcCommand = line.split(" ").map(Number);
    rl.close();
  }
});

const choiceOneUpsideDown = (arr) => {
  const rowLength = arr.length;
  const ansArr = [];
  for (let i = 0; i < rowLength; i++) {
    ansArr.push(arr.pop());
  }
  return ansArr;
};

const choiceTwoLeftRightInversion = (arr) => {
  const rowLength = arr.length;
  const ansArr = [];
  for (let i = 0; i < rowLength; i++) {
    ansArr.push(arr.shift().reverse());
  }
  return ansArr;
};

const rotateRight = (loop, ansArr, givenArray) => {
  let flattenedArr = [];
  const colLen = givenArray[0].length;
  const rowLen = givenArray.length;

  // take out
  for (let j = loop; j < colLen - loop; j++) {
    flattenedArr.push(givenArray[loop][j]);
  }
  flattenedArr.pop();
  for (let i = loop; i < rowLen - loop; i++) {
    flattenedArr.push(givenArray[i][colLen - loop - 1]);
  }
  flattenedArr.pop();
  for (let j = colLen - loop - 1; j >= loop; j--) {
    flattenedArr.push(givenArray[rowLen - loop - 1][j]);
  }
  flattenedArr.pop();
  for (let i = rowLen - loop - 1; i >= loop; i--) {
    flattenedArr.push(givenArray[i][loop]);
  }
  flattenedArr.pop();

  // fill in

  const ansArrRowLen = ansArr.length;
  const ansArrColLen = ansArr[0].length;

  for (let i = loop; i < ansArrRowLen - loop - 1; i++) {
    ansArr[i][ansArrColLen - loop - 1] = flattenedArr.shift();
  }
  for (let j = ansArrColLen - loop - 1; j > loop; j--) {
    ansArr[ansArrRowLen - loop - 1][j] = flattenedArr.shift();
  }
  for (let i = ansArrRowLen - loop - 1; i > loop; i--) {
    ansArr[i][loop] = flattenedArr.shift();
  }
  for (let j = loop; j < ansArrColLen - loop - 1; j++) {
    ansArr[loop][j] = flattenedArr.shift();
  }

  return ansArr;
};

const choiceThreeRotateRight = (givenArray) => {
  const colLength = givenArray[0].length;
  const rowLength = givenArray.length;
  let ansArr = Array.from({ length: colLength }, () =>
    Array(rowLength).fill(0)
  );

  for (let loop = 0; loop < Math.min(rowLength, colLength) / 2; loop++) {
    ansArr = rotateRight(loop, ansArr, givenArray);
  }

  return ansArr;
};

const choiceFourRotateLeft = (givenArray) => {
  const colLength = givenArray[0].length;
  const rowLength = givenArray.length;

  let ansArr = Array.from({ length: colLength }, () =>
    Array(rowLength).fill(0)
  );

  for (let loop = 0; loop < Math.min(rowLength, colLength) / 2; loop++) {
    ansArr = rotateRight(loop, ansArr, givenArray);
  }
  const nextArr = choiceOneUpsideDown(ansArr);
  const finalArr = choiceTwoLeftRightInversion(nextArr);

  return finalArr;
};

const chunkArrays = (givenArray) => {
  const colLength = givenArray[0].length;
  const rowLength = givenArray.length;

  let leftArr = [];
  let rightArr = [];

  for (let i = 0; i < rowLength; i++) {
    const larr = [];
    const rarr = [];
    for (let j = 0; j < colLength; j++) {
      if (j < colLength / 2) larr.push(givenArray[i][j]);
      else rarr.push(givenArray[i][j]);
    }
    leftArr.push(larr);
    rightArr.push(rarr);
  }

  return [leftArr, rightArr];
};

const chocieFiveRotateRightInChuncks = (givenArray) => {
  const rowLength = givenArray.length;

  const [leftArr, rightArr] = chunkArrays(givenArray);
  const finalArr = [];
  const tempRightArr = [];
  for (let i = 0; i < rowLength / 2; i++) {
    finalArr.push(leftArr[i + rowLength / 2].concat(leftArr[i]));
    tempRightArr.push(rightArr[i + rowLength / 2].concat(rightArr[i]));
  }

  return finalArr.concat(tempRightArr);
};

const chocieSixRotateLeftInChuncks = (givenArray) => {
  const rowLength = givenArray.length;

  let [leftArr, rightArr] = chunkArrays(givenArray);
  const finalArr = [];
  const tempRightArr = [];
  for (let i = 0; i < rowLength / 2; i++) {
    finalArr.push(leftArr[i].concat(leftArr[i + rowLength / 2]));
    tempRightArr.push(rightArr[i].concat(rightArr[i + rowLength / 2]));
  }
  givenArray = tempRightArr.concat(finalArr);

  return givenArray;
};

rl.on("close", function () {
  while (calcCommand.length) {
    const command = calcCommand.shift(0);
    switch (command) {
      case 1:
        givenArray = choiceOneUpsideDown(givenArray);
        break;
      case 2:
        givenArray = choiceTwoLeftRightInversion(givenArray);
        break;
      case 3:
        givenArray = choiceThreeRotateRight(givenArray);
        break;
      case 4:
        givenArray = choiceFourRotateLeft(givenArray);
        break;
      case 5:
        givenArray = chocieFiveRotateRightInChuncks(givenArray);
        break;
      case 6:
        givenArray = chocieSixRotateLeftInChuncks(givenArray);
        break;
      default:
        break;
    }
  }
  console.log(givenArray.map((row) => row.join(" ")).join("\n"));
  process.exit();
});
