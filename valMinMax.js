function minMaxArray(lista) {
    if (lista.length === 0) return "array vuoto";

    let min = lista[0];
    let max = lista[0];

    for(let i = 1; i < lista.length; i++){
        if (lista[i] < min) min = lista[i];
        if (lista[i] > max) max = lista[i];
    }
    return {min, max};
}
console.log("4.2) Min e Max di [3, 7, 2, 9, 5] =", minMaxArray([3, 7, 2, 9, 5]));