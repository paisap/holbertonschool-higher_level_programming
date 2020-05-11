#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c || 'X');
      }
      console.log();
    }
  }
};
