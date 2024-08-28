any(iterable)
#Retorna True se algum elemento de iterable for verdadeiro. Se iterable estiver vazio, retorna False. Equivalente a:
def any(iterable):
    for element in iterable:
        if element:
            return True
        return False
