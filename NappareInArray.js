function contaOccorrenze(array, numeroCercato) {
let contatore = 0;
for (let i = 0; i < array.length; i++) {
if (array[i] === numeroCercato) {
contatore++;
}
}
return contatore;
}
console.log("3) Occorrenze del numero 3 in [1,3,2,3,4,3] =", contaOccorrenze([1, 3, 2, 3, 4, 3], 3));