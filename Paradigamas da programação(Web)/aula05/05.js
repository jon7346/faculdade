function listar(){
    var numero = document.getElementById('numero').value 
    let resultado = '' 
   for (let i = 1 ; i < parseInt(numero) ; ++i){
    resultado += i + ' ' 
   }
  alert(resultado)
}
