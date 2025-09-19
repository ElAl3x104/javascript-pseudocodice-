const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let array = [];
let N;
let numeroCercato;
let step = 0;

console.log("Inserisci la dimensione dell'array:");

rl.on('line', (input) => {
  if (step === 0) {
    N = parseInt(input);
    if (isNaN(N) || N <= 0) {
      console.log("Inserisci un numero valido per la dimensione dell'array:");
      return;
    }
    console.log(`Inserisci ${N} elementi:`);
    step++;
  } else if (step > 0 && step <= N) {
    let elemento = parseInt(input);
    if (isNaN(elemento)) {
      console.log("Inserisci un numero valido:");
      return;
    }
    array.push(elemento);
    step++;
    if (step > N) {
      console.log("Inserisci il numero da cercare:");
    }
  } else if (step === N + 1) {
    numeroCercato = parseInt(input);
    if (isNaN(numeroCercato)) {
      console.log("Inserisci un numero valido:");
      return;
    }

    let contatore = 0;
    for (let i = 0; i < N; i++) {
      if (array[i] === numeroCercato) {
        contatore++;
      }
    }

    console.log("Numero occorrenze trovate:", contatore);
    rl.close();
  }
});
