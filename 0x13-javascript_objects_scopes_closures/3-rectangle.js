#!/usr/bin/node
module.exports = class Rectangle {
  constructor (height, width) {
    if (height > 0 && width > 0) {
      this.height = height;
      this.width = width;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) console.log('X'.repeat(this.height));
  }
};
