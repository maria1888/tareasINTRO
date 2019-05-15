class Grafico(object):
    def __init__(self):
        pass

    def grafico(self,lista):
        if isinstance (lista,list):
            return self.grafico_aux(lista,0,0,)
        else: return "error"

    def grafico_aux(self,lista,indice,ran_colum):
        if indice== len(lista):
            return ran_colum
        elif lista[indice]<lista[indice+1]:
            return self.grafico_aux(lista,indice+1,(lista[indice+1]))
        else : return self.grafico_aux(lista,indie+1,(lista[indice]))

    def aux2(self,lista,columna,filas,ran_colum,matriz,indice):
        columna=0
        filas=0
        len(matriz[0])=ran_colum
        len(matriz)=len(lista)
        matriz=[]
        indice=0
        if fila== len(matriz):
            return matriz
        matriz[filas][columna]="*"
        elif columna<=lista[indice]:
            return self.aux2(lista,columna+1,filas+1,ran_colum,[matriz[fila][columna]],indice)
        elif columna==len(matriz[0]):
            return self.aux2(lista,0,filas+1,ran_colum,[matriz[fila][columna]],indice+1)
