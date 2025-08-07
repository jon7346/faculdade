// Passos do algoritmo:
// Percorrer a lista: O algoritmo começa do início da lista e percorre os elementos da esquerda para a direita.
// Comparação entre pares: Para cada par de elementos consecutivos, ele compara se o primeiro é maior que o segundo.
// Troca de posição: Se o primeiro elemento for maior que o segundo, eles trocam de posição.
// Repetição do processo: Esse processo de percorrer a lista e realizar comparações e trocas é repetido várias vezes. A cada iteração, o maior valor entre os elementos restantes "sobe" para sua posição correta.
// Parar quando ordenado: O algoritmo continua até que não sejam mais necessárias trocas, ou seja, quando a lista estiver ordenada.
let arr = [1, 4, 7, 45, 7,43, 44, 25, 6, 4, 6, 9],
    sorted = false;

while(!sorted) {
  sorted = true;
  for(var i=0; i < arr.length; i++) {
    if(arr[i] < arr[i-1]) {
      let temp = arr[i];
      arr[i] = arr[i-1];
      arr[i-1] = temp;
      sorted = false;
    }
  }
}

