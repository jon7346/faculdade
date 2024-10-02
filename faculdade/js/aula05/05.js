function listar(){
    var numero = 0;
    let lista = []
   numero = document.getElementById("numero");

   for (let i = 1 ; i < parseInt(numero) ; ++i){
    lista.push(i)
   }
   alert(lista.join(' ,'))
}
