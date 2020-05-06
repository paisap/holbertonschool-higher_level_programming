#!/usr/bin/node
function fac (x) {
  if (x < 0) return;
  if (x === 0) return 1;
  return x * fac(x - 1);
}
const x = process.argv[2];
(x === undefined || isNaN(x)) ? console.log('1') : console.log(fac(x));
