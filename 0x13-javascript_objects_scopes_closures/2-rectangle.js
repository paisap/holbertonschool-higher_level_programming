#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    if (height > 0 && width > 0) {
      this.width = width;
      this.height = height;
    }
  }
};
