#!/usr/bin/node
const x = parseInt(process.argv[2]);
const y = 'X';
if (x === parseInt(x)) {
  for (let i = 0; i < x; i++) console.log(y.repeat(x));
} else { console.log('Missing size'); }
