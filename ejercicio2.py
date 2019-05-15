class Permutaciones(object):
    def __init__(self):
        pass

    def permutaciones(self,n,x):
        if isinstance (n,int) and isinstance(x,int):
            return self.aux(n,x,n-1,0)
        else : return "error"

    def aux(self,n,x,auxiliar,result):
        if auxiliar==0:
            return result
        else : return self.aux(n,x,auxiliar-1,(n-auxiliar))

    def aux2(self,n,x,auxiliar,result2):
        if auxiliar==0:
            return (self.aux)//result2
        m=n-x
        else : return self.aux2(n,x,auxiliar-1,(m-auxiliar))
