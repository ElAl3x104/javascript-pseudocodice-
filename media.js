function mediaNumeri(lista){
    let somma = 0;
    let conteggio = 0;
    for (let numero of lista){
        somma += numero;
        conteggio++;
    }
    if (conteggio > 0) {
        return somma / conteggio;
    }else{
        return "nessun numero inserito";
    }
}
console.log("3) Media numeri [2, 4, 6, 0] =", mediaNumeri([2, 4, 6, 0]));
console.log("3) Media numeri [0] =", mediaNumeri([0]));