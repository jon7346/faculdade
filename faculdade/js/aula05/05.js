<<<<<<< HEAD
Array('lista')  = []
var numero = 0 ,resultado = 0;

function adicionar(){
 numero = document.getElementById('numero')
 resultado = document.getElementById('resultado');
 for(let i = 0 , i < numero, i++,)
=======
function listar(){
    var numero = 0;
    let lista = []
   numero = document.getElementById("numero");

   for (let i = 1 ; i < parseInt(numero) ; ++i){
    lista.push(i)
   }
   alert(lista.join(' ,'))
>>>>>>> 940fa9117f2530cac5269345a1c5bd0eb31d237c
}
