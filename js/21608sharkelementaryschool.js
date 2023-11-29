const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let classroomSize = 0;
let seats = [];
let favoriteFriends = new Map();

let seated = new Map();
let points = 0;

const dirC = [0, -1, 1, 0];
const dirR = [-1, 0, 0, 1];
const DIRECTIONSIZE = 4;
const satisfactionPoints = [0, 1, 10, 100, 1000];

rl.on("line", function (line) {
  if (classroomSize === 0) classroomSize = Number(line);
  else if (favoriteFriends.length !== classroomSize ** classroomSize) {
    const thisLine = line.split(" ").map(Number);
    favoriteFriends.set(thisLine[0], thisLine.slice(1));
  }
});

const isBound = (newR, newC) => {
  if (newC < 0 || newR < 0 || newC >= classroomSize || newR >= classroomSize)
    return false;
  return true;
};

// 주어진 자리의 동서남북 중 가능한 자리를 리스트로 반환
const findNearPossibleSeats = (seat) => {
  let possibleSeats = [];
  for (let i = 0; i < DIRECTIONSIZE; i++) {
    const newR = seat[0] + dirR[i];
    const newC = seat[1] + dirC[i];
    if (isBound(newR, newC) && seats[newR][newC] === 0) {
      possibleSeats.push([newR, newC]);
    }
  }
  return possibleSeats;
};

// 주어진 자리 근처 내 친구들이 몇명인지 확인
const countMyFriendsNearSeat = (seat, me) => {
  const myFavFriends = favoriteFriends.get(me);
  let friendCount = 0;
  for (let i = 0; i < DIRECTIONSIZE; i++) {
    const newR = seat[0] + dirR[i];
    const newC = seat[1] + dirC[i];
    if (isBound(newR, newC) && myFavFriends.includes(seats[newR][newC]))
      friendCount++;
  }
  return friendCount;
};

// 첫번쨰 seat가 더 적은지 (조건3)
const isSmallerThan = ([r, c], [rr, cc]) => {
  if (r < rr) return true;
  if (r === rr) if (c < cc) return true;
  return false;
};

// 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다
const getMyBestSeat = (me) => {
  const myFavFriends = favoriteFriends.get(me);
  if (myFavFriends.length === 0) return;
  let bestFriendCount = 0;
  let bestSeat = [-1, -1];
  let bestNearEmptyCount = 0;
  myFavFriends.map((friend) => {
    // 그 친구가 앉아있다면
    if (seated.get(friend).length) {
      // find friend의 동서남북중 앉을 수 있는 자리
      const [r, c] = seated.get(friend);
      const possibleSeats = findNearPossibleSeats([r, c]);
      possibleSeats.map((seat) => {
        // 각 가능한 자리에서 최대 friendCount 찾기
        const friendCount = countMyFriendsNearSeat(seat, me);
        if (friendCount > bestFriendCount) {
          bestFriendCount = friendCount;
          bestSeat = seat;
          bestNearEmptyCount = findNearPossibleSeats(seat).length;
        } else if (friendCount === bestFriendCount) {
          let friendCountEmptySeats = findNearPossibleSeats(seat).length;
          let bestFriendCountEmptySeats =
            findNearPossibleSeats(bestSeat).length;

          if (friendCountEmptySeats > bestFriendCountEmptySeats) {
            if (friendCountEmptySeats > bestNearEmptyCount) {
              bestSeat = seat;
              bestNearEmptyCount = bestFriendCountEmptySeats;
            }
          } else if (friendCountEmptySeats === bestFriendCountEmptySeats) {
            if (isSmallerThan(seat, bestSeat)) {
              bestSeat = seat;
            }
          }
        }
      });
    }
  });
  return bestSeat;
};

// 제일 많은 아무 자리 찾기
const getAnyEmptySeat = () => {
  let bestSeat = [-1, -1];
  let nearEmptyBestCount = -1;
  for (let i = 0; i < classroomSize; i++) {
    for (let j = 0; j < classroomSize; j++) {
      if (seats[i][j] === 0) {
        const nearEmptyCount = findNearPossibleSeats([i, j]).length;
        if (nearEmptyCount === 4) return [i, j];
        if (nearEmptyCount > nearEmptyBestCount) {
          nearEmptyBestCount = nearEmptyCount;
          bestSeat = [i, j];
        }
      }
    }
  }
  return bestSeat;
};

const countSatisfactionPoints = () => {
  for (let i = 0; i < classroomSize; i++) {
    for (let j = 0; j < classroomSize; j++) {
      let friendCount = 0;
      const me = seats[i][j];
      const myFavFriends = favoriteFriends.get(me);
      for (let d = 0; d < DIRECTIONSIZE; d++) {
        const newI = i + dirR[d];
        const newJ = j + dirC[d];
        if (isBound(newI, newJ)) {
          const checkingFriend = seats[newI][newJ];
          if (myFavFriends.includes(checkingFriend)) {
            friendCount++;
          }
        }
      }
      points += satisfactionPoints[friendCount];
    }
  }
  return points;
};
rl.on("close", function () {
  seats = Array.from({ length: classroomSize }, () =>
    Array(classroomSize).fill(0)
  );
  for (let i = 1; i <= classroomSize * classroomSize; i++) {
    seated.set(i, []);
  }

  favoriteFriends.forEach((_, person) => {
    if (person === 0) return;
    let personSeat = getMyBestSeat(person);
    if (personSeat[0] === -1 && personSeat[1] === -1) {
      personSeat = getAnyEmptySeat();
    }
    seated.set(person, personSeat);
    seats[personSeat[0]][personSeat[1]] = person;
  });
  console.log(countSatisfactionPoints());
  process.exit();
});

// TEST CODES:

// let classroomSize = 3;
// let seats = [
//   [0, 0, 0],
//   [0, 0, 0],
//   [0, 0, 0],
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

// // seated.set(2, [0, 1]);
// // seated.set(1, [2, 1]);

// // // 자리 (1, 1) 근처 앉을 수 있는 자리 리스트
// // console.log(findNearPossibleSeats([1, 1]));
// // // 자리 (1, 1) 근처 나 (4) 친구가 몇명있는지 확인
// // console.log(countMyFriendsNearSeat([1, 1], 4));

// console.log(matchCondition(4));
// console.log(solve())
