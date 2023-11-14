#!/usr/bin/node
//  a class Square that defines a square and inherits from Square of 5-square.js

const ExSquare = require('./5-square');

class Square extends ExSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
