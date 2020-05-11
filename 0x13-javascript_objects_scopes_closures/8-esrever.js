#!/usr/bin/node
exports.esrever = function (list) {
  let aux = list[0];
  for (let i = 0; i < list.length / 2; i++) {
    aux = list[list.length - i - 1];
    list[list.length - i - 1] = list[i];
    list[i] = aux;
  }
  return list;
};
