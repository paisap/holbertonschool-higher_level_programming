#!/usr/bin/node
const list = require('./100-data').list;
let i = 0;
const map1 = list.map(x => x * i++);
console.log(list);
console.log(map1);
