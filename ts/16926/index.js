// var input = require("fs").readFileSync("/dev/stdin").toString().split(" ");
/** --------------------- INPUT --------------------- */
var path = require("path");
var input = require("fs")
    .readFileSync(path.resolve(__dirname, "input.txt"))
    .toString()
    .split("\n");
var _a = input[0].split(" ").map(Number), rowCount = _a[0], colCount = _a[1], rotationCount = _a[2];
var arrays = input.slice(1, rowCount).map(function (row) {
    return row.split(" ");
});
console.log("Your input is " + rowCount, colCount, rotationCount);
console.log("arrays: ", arrays);
/** --------------------- PURES --------------------- */
var getIterationCount = function (colCount) {
    return colCount / 2;
};
var iterate = function (arrays, layer, rowCount, colCount) {
    var row;
    var col;
    var endCol = colCount - layer;
    var endRow = rowCount - layer;
    for (row = layer; row < endRow; row++) {
        for (col = layer; col < endCol; col++) {
            console.log("iam at ", arrays[row][col]);
        }
    }
};
var iterateAndCompress = function (colCount) { };
/** --------------------- EXECUTION --------------------- */
var ans = iterate(arrays, 0, rowCount, colCount);
console.log("✨: ", ans);
