const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function sommaArray(array) {
  let somma = 0;
  for (let i = 0; i < array.length; i++) {
    somma += array[i];
  }
  return somma;
}

async function main() {
  function question(prompt) {
    return new Promise(resolve => rl.question(prompt, resolve));
  }

  let N = parseInt(await question("Inserisci la dimensione dell'array: "));
  while (isNaN(N) || N <= 0) {
    N = parseInt(await question("Inserisci un numero valido per la dimensione dell'array: "));
  }

  let array = [];
  for (let i = 0; i < N; i++) {
    let num = parseInt(await question(`Inserisci elemento ${i + 1}: `));
    while (isNaN(num)) {
      num = parseInt(await question("Inserisci un numero valido: "));
    }
    array.push(num);
  }

  const somma = sommaArray(array);
  console.log("La somma degli elementi è:", somma);

  rl.close();
}

main();
