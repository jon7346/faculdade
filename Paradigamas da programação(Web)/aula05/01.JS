var X = prompt('insira um numero:')
var Y = prompt('insira outro numero para comparar: ')

function comparar() {
    if (parseInt(X) > parseInt(Y) ){
        alert("o maior numero é "+ X);
    }
    else {
    alert("o maior numero é " + Y);
    }
}
  comparar(X,Y);