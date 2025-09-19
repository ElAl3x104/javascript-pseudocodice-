const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function trovaMinimoEMassimo(array) {
  if (array.length === 0) {
    throw new Error("Array vuoto: impossibile trovare minimo e massimo");
  }
  let minimo = array[0];
  let massimo = array[0];
  for (let i = 1; i < array.length; i++) {
    if (array[i] < minimo) minimo = array[i];
    if (array[i] > massimo) massimo = array[i];
  }
  return { minimo, massimo };
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

  try {
    const { minimo, massimo } = trovaMinimoEMassimo(array);
    console.log(`Minimo: ${minimo}`);
    console.log(`Massimo: ${massimo}`);
  } catch (error) {
    console.log(error.message);
  }

  rl.close();
}

main();
