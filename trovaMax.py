const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let array = [];
let N;
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
      const massimo = trovaMassimo(array, N);
      console.log("Il valore massimo è:", massimo);
      rl.close();
    }
  }
});

function trovaMassimo(arr, n) {
  let massimo = arr[0];
  for (let i = 1; i < n; i++) {
    if (arr[i] > massimo) {
      massimo = arr[i];
    }
  }
  return massimo;
}
