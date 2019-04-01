def intercambiar(lista):
    impar = lambda num : lista[0]%2==1
    par = lambda num : lista[0]%2==0
    
    if isinstance (lista, list):
        return aux(lista, impar,par)
    else : return "error"


def aux(lista, impar,par):
    if lista==[]:
        return []
    elif impar (lista[0]):
        return [lista[0]] + aux(lista[2:], impar,par)
    elif par (lista[0]):
        return [lista[1]] + aux(lista[2:], impar,par)
        

