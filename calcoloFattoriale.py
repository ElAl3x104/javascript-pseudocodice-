const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function calcolaFattoriale(n) {
  let fattoriale = 1;
  for (let i = 1; i <= n; i++) {
    fattoriale *= i;
  }
  return fattoriale;
}

rl.question('Inserisci un numero intero non negativo per calcolare il fattoriale: ', (input) => {
  const n = parseInt(input);
  if (isNaN(n) || n < 0) {
    console.log("Devi inserire un numero intero non negativo!");
  } else {
    const risultato = calcolaFattoriale(n);
    console.log(`Il fattoriale di ${n} è ${risultato}`);
  }
  rl.close();
});
