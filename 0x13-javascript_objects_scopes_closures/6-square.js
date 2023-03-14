#!/usr/bin/node

const oldSq = require('./5-square');
class Square extends oldSq {
  charPrint (C) {
    if (!C) {
      C = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(C.repeat(this.width));
    }
  }
}
module.exports = Square;
