const readline = require("readline");

function compareBoards(board, compareBoard) {
  let differences = 0;
  for (var ci = 0; ci < 8; ci++) {
    for (var cj = 0; cj < 8; cj++) {
      if (compareBoard[ci][cj] !== board[ci][cj]) {
        differences++;
      }
    }
  }
  return differences;
}
function solution(chessboard) {
  let minimumChanges = m * n;
  const rightBoard = [
    ["W", "B", "W", "B", "W", "B", "W", "B", "W"],
    ["B", "W", "B", "W", "B", "W", "B", "W", "B"],
    ["W", "B", "W", "B", "W", "B", "W", "B", "W"],
    ["B", "W", "B", "W", "B", "W", "B", "W", "B"],
    ["W", "B", "W", "B", "W", "B", "W", "B", "W"],
    ["B", "W", "B", "W", "B", "W", "B", "W", "B"],
    ["W", "B", "W", "B", "W", "B", "W", "B", "W"],
    ["B", "W", "B", "W", "B", "W", "B", "W", "B"],
  ];
  const whiteBoard = [];
  const blackBoard = [];

  for (var t = 0; t < 8; t++) {
    whiteBoard.push(rightBoard[t].slice(0, 8));
    blackBoard.push(rightBoard[t].slice(1, 9));
  }
  for (let i = 0; i < m - 7; i++) {
    for (let j = 0; j < n - 7; j++) {
      let tempChessboard = [];
      for (var bi = i; bi < i + 8; bi++) {
        var row = chessboard[bi].slice(j, j + 8);
        tempChessboard.push(row);
      }
      const isStartsWithWhite = tempChessboard[0][0] === "W";
      let originalDiff = compareBoards(
        tempChessboard,
        isStartsWithWhite ? whiteBoard : blackBoard
      );
      isStartsWithWhite
        ? (tempChessboard[0][0] = "B")
        : (tempChessboard[0][0] = "W");
      let changedDiff = compareBoards(
        tempChessboard,
        isStartsWithWhite ? blackBoard : whiteBoard
      );
      if (minimumChanges > originalDiff) minimumChanges = originalDiff;
      if (minimumChanges > changedDiff+1) minimumChanges = changedDiff+1;
    }
  }
  console.log(minimumChanges);
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let m = 0;
let n = 0;
let chessboard = [];

rl.on("line", function (line) {
  if (m === 0) {
    const inputVal = line.split(" ").map((v) => parseInt(v));
    m = inputVal[0];
    n = inputVal[1];
  } else {
    const chessboardLine = line.split("");
    chessboard.push(chessboardLine);
    if (chessboard.length === m) {
      solution(chessboard);
      rl.close();
    }
  }
});
