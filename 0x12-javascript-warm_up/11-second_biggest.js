#!/usr/bin/node

if (process.argv.lenght <= 3) {
  console.log(0);
} else {
  const arr = process.argv
    .map(Number);
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
