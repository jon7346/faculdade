all()
#Retorna True se todos os elementos de iterable são verdadeiros (ou se iterable estiver vazio). Equivalente a:
def all(iterable):
    for element in iterable:
        if not element:
             return False
    return True
'''''
awaitable anext(async_iterator)
awaitable anext(async_iterator, default)

Quando aguardado, retorna o próximo item do iterador assíncrono fornecido, 
ou default se fornecido e o iterador for esgotado.

Esta é a variante assíncrona do next() embutido, e se comporta de forma semelhante.

Isso chama o método __anext__() de async_iterator, retornando um aguardável. Ao aguardar isso,
retorna o próximo valor do iterador. Se default for fornecido, ele será retornado se o itera-
dor for esgotado, caso contrário, a exceção StopAsyncIteration será levantada.
'''''
