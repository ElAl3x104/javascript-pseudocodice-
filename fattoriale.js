// calcolo fattoriale
function fattoriale(n) {
    let risultato = 1;
    for (let i = 1; i<= n; i++){
        risultato *= i;
    }
    return risultato;
}
console.log("1) Fattoriale di 5 =", fattoriale(5));