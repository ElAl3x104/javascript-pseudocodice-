function sommaNumeriPari(N) {
    let somma = 0;
    for (let i = 1; i <= N; i++) {
        let numeroPari = i * 2; // Questo calcola il numero pari
        somma += numeroPari; // Somma il numero pari
    }
    return somma;
}

// Passa il parametro 5 per sommare i primi 5 numeri pari
console.log("2) Somma dei primi 5 numeri pari =", sommaNumeriPari(5));
