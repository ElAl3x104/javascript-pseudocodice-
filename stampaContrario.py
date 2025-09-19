const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function stampaArrayAlContrario(array) {
  console.log("Numeri in array al contrario:");
  for (let i = array.length - 1; i >= 0; i--) {
    console.log(array[i]);
  }
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

  stampaArrayAlContrario(array);

  rl.close();
}

main();
