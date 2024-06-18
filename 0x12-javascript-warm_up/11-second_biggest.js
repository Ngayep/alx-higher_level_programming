#!/usr/bin/node

if (process.argv.lenght <= 3) {
  console.log(0);
} else {
  const arr = process.argv.map(Number);
  const second = arr.sort(function (a, b) { return a - b; })[process.argv.length - 2];
  console.log(second);
}
