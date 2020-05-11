#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (height > 0 && width > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
