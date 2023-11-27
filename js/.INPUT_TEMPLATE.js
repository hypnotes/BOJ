function solution(input) {
  console.log(input);
}

import { createInterface } from "readline";
const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;
// let list = [];
rl.on("line", function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  // 한줄: list = input.split(' ').map((el) => Number(el));

  // 형변환, 구분자(띄어쓰기)기준으로 배열에 삽입
  // input.forEach((val) => {
  //     list.push(val.split(' ').map((el) => parseInt(el)));
  //  });

  solution(input);
  process.exit();
});


// https://aiday.tistory.com/103