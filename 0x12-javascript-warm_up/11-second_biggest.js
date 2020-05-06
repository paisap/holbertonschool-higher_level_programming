#!/usr/bin/node
const matrix = [0];
for (let i = 2; i < process.argv.length; i++) {
  matrix[i - 2] = parseInt(process.argv[i]);
}
let mayor = matrix[0];
let menor = mayor;
for (let i = 0; i < matrix.length; i++) {
  if (matrix[i] > mayor) {
    menor = mayor;
    mayor = matrix[i];
  } else if (matrix[i] > menor && matrix[i] !== mayor) {
    menor = matrix[i];
  }
}
(process.argv.length <= 3) ? console.log(0) : console.log(menor);
