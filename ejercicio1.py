class Matriz(object):
    def __init__(self):
        pass

    def matriz(self,numero):
        if isinstance (numero,int):
            return self.matriz_aux(numero,[],0,0,1)
        else : return "error no cumple con lo requerido"

    def matriz_aux(self,numero,matriz,fila,columna,elemento):
        len(matriz)=numero
        len(matriz[0])=numero
        if fila == len(matriz):
            return matriz
        elif c == len(matriz[0]):
            return self.matriz_aux (numero[matriz[fila][columna] + elemento],fila+1,0,1)
        matriz[fila][columna]="*"
        elif fila>= 1:
            return self.matriz_aux(numero,[matriz[fila][columna],matriz[fila][columna]+elemento],fila,columna+1,elemento+1)
