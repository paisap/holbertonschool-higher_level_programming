#!usr/bin/node
exports.callMeMoby = function (x, theFcuntion) {
  for (let i = 0; i < x; i++) {
    theFcuntion();
  }
};
