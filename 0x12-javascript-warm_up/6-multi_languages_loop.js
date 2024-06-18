#!/usr/bin/node

const myLines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
while (typeof (myLines[0]) !== 'undefined') {
  console.log(myLines.shift());
}
