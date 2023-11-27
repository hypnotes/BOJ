const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let classroomSize = 0;
let seats = [];
let favoriteFriends = new Map();

let seated = new Map();

const dirC = [-1, 0, 1, 0];
const dirR = [0, -1, 0, 1];
const DIRECTIONSIZE = 4;

rl.on("line", function (line) {
  if (classroomSize === 0) classroomSize = Number(line);
  else {
    const [a, b, c, d, e] = line.split(" ").map(Number);
    favoriteFriends.set(a, [b, c, d, e]);
  }
});

const isBound = (newR, newC) => {
  if (newC < 0 || newR < 0 || newC >= classroomSize || newR >= classroomSize)
    return false;
  return true;
};

const findClosestPossibleSeats = (r, c) => {
  let closestPossibleSeats = [];
  for (let i = 0; i < DIRECTIONSIZE; i++) {
    const newC = dirC[i] + c;
    const newR = dirR[i] + r;
    if (isBound(newR, newC) && !seats[newR][newC])
      closestPossibleSeats.push([newR, newC]);
  }
  if (!closestPossibleSeats.length) {
    return [[-1, -1]];
  }
  return closestPossibleSeats;
};

const findHowManyFriendsNear = (r, c, me) => {
  let friendCount = 0;
  for (let i = 0; i < DIRECTIONSIZE; i++) {
    const newC = dirC[i] + c;
    const newR = dirR[i] + r;
    if (
      isBound(newR, newC) &&
      favoriteFriends.get(me).includes(seats[newR][newC])
    ) {
      friendCount++;
    }
  }
  return friendCount;
};

const findMostFriendsSeat = (me) => {
  let bestSeat = [-1, -1];
  let bestSeatFriend = 0;
  // TODO: make history of already visited seats
  favoriteFriends.get(me).map((friend) => {
    if (seated.get(friend).length) {
      const [r, c] = seated.get(friend);
      findClosestPossibleSeats(r, c).map((seat) => {
        const [newR, newC] = seat;
        const friendCount = findHowManyFriendsNear(newR, newC, me);
        if (friendCount > bestSeatFriend) {
          bestSeatFriend = friendCount;
          bestSeat = seat;
        } else if (friendCount === bestSeatFriend) {
          if (
            findClosestPossibleSeats(newR, newC).length <
            findClosestPossibleSeats(bestSeat[0], bestSeat[1]).length
          ) {
            bestSeat = seat;
          } else if (newR < bestSeat[0]) {
            bestSeat = seat;
          } else if (newR === bestSeat[0]) {
            if (newC < bestSeat[1]) {
              bestSeat = seat;
            }
          }
        }
      });
    }
  });
  return bestSeat;
};

rl.on("close", function () {
  seats = Array.from({ length: classroomSize }, () =>
    Array(classroomSize).fill(0)
  );
  for (let i = 1; i <= classroomSize * classroomSize; i++) {
    seated.set(i, []);
  }
  favoriteFriends.forEach((friend, k) => {
    console.log("working on ", k);
    let [r, c] = findMostFriendsSeat(k);
    if (r === -1 && c === -1) {
      let bestSeat = [-1, -1];
      let emptyCountBest = 0;
      for (let i = 0; i < classroomSize; i++) {
        for (let j = 0; j < classroomSize; j++) {
          if (!seats[i][j]) {
            const emptyCount = findClosestPossibleSeats(i, j).length;
            if (emptyCount > emptyCountBest) {
              bestSeat = [i, j];
              emptyCountBest = emptyCount;
            }
          }
        }
      }
      [r, c] = bestSeat;
    }
    seats[r][c] = k;
    seated.set(k, [r, c]);
    console.log("seated", k, "at", r, c);
    console.log(seats);
  });

  console.log(seats);
});

// TEST CODES:

// let classroomSize = 3;
// let seats = [
//   [0, 2, 0],
//   [0, 0, 0],
//   [0, 1, 0],
// ];
// let favoriteFriends = {
//   4: [2, 5, 1, 7],
//   3: [1, 9, 4, 5],
//   9: [8, 1, 2, 3],
//   8: [1, 9, 3, 4],
//   7: [2, 3, 4, 8],
//   1: [9, 2, 5, 7],
//   6: [5, 2, 3, 4],
//   5: [1, 9, 2, 8],
//   2: [9, 3, 1, 4],
// };

// let seated = new Map();
// for (let i = 1; i <= classroomSize * classroomSize; i++) {
//   seated.set(i, []);
// }

// seated.set(2, [0, 1]);
// seated.set(1, [2, 1]);

// console.log(
//   "closest possible seat near (0,0):",
//   findClosestPossibleSeats(1, 1)
// );
// // console.log(findHowManyFriendsNear(1, 1, 4));
// console.log(findMostFriendsSeat(4));
