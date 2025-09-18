function calcolaFattoriale(n) {
let fattoriale = 1;
for (let i = 1; i <= n; i++) {
fattoriale *= i;
}
return fattoriale;
}
let numero = 6;
let risultatoFattoriale = calcolaFattoriale(numero);
console.log(`5) Il fattoriale di ${numero} è ${risultatoFattoriale}`);