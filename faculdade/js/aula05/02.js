var valor1 = 0 , valor2 = 0 ;

function dividir() {
    valor1 = document.getElementById('valor1').value
    valor2 = document.getElementById('valor2').value
    document.getElementById('resultado').value = valor1 / valor2
}
function multiplicar() {
    valor1 = document.getElementById('valor1').value
    valor2 = document.getElementById('valor2').value
    document.getElementById('resultado').value = valor1 * valor2
}

function subtrair() {
    valor1 = document.getElementById('valor1').value
    valor2 = document.getElementById('valor2').value
    document.getElementById('resultado').value = valor1 - valor2
}

function somar() {
    valor1 = document.getElementById('valor1').value
    valor2 = document.getElementById('valor2').value
    document.getElementById('resultado').value = parseInt(valor1) + parseInt(valor2)
}
