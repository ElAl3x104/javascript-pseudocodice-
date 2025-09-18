function trovaMassimo(array) {
if (array.length === 0) return null;

let max = array[0];
for (let i = 1; i < array.length; i++) {
if (array[i] > max) {
max = array[i];
}
}
return max;
}
let arr2 = [15, 3, 27, 8, 19];
let maxRisultato = trovaMassimo(arr2);
console.log("7) Massimo dell’array =", maxRisultato);