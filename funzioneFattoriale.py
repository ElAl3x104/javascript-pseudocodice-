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

rl.question("Inserisci un numero per calcolare il fattoriale: ", (input) => {
  const numero = parseInt(input);
  if (isNaN(numero) || numero < 0) {
    console.log("Per favore inserisci un numero intero non negativo.");
  } else {
    const risultato = calcolaFattoriale(numero);
    console.log(`Il fattoriale di ${numero} è ${risultato}`);
  }
  rl.close();
});
