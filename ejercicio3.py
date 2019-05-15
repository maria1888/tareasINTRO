class Cuadrado_Magico(object):
    def __init__(self):
        pass

    def es_magico(self,matriz):
        if (isinstance(matriz,list) and len(matriz)=len(matriz[0])):
            return self.suma_fila(matriz,0,0,0),
                    self.suma_columna(matriz,0,0,0)
                    self.suma_diagonal(matriz,0,0,0,)
                    self.suma_antidi(matriz,0,len(matriz[0])-1,0)
        else: return "error"

    def suma_fila(self,matriz,fila,columna,result1):
        if fila==len(matriz):
            return result1
        elif columna==len(matriz[0]):
            return self.suma_fila(matriz,fila+1,0,(matriz[fila][columna]))
        else: return self.suma_fila(matriz,fila,columna+1,(matriz[fila][columna]))

    def suma_columna(self,matriz,fila,columna,result2):
        if fila==len(matriz):
            return result2
        elif columna==len(matriz[0]):
            return
        else: return

    def suma_diagonal(self,matriz,fila,columna,result3):
        if fila== len(matriz):
            return result3
        else : return self.suma_diagonal(matriz,fila+1,columna+1,(matriz[fila][columna]))

    def suma_antidi(self,matriz,fila,columna,result4):
        if fila==len(matriz):
            return result4
        elif isinstance (matriz,list):
            return self.suma_antidi(matriz,fila,columna,(matriz[fila][columna]))
        else: return self.suma_antidi(matriz,fila+1,columna-1,(matriz[fila][columna]))
            
