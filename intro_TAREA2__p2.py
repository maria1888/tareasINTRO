def palindromo(num):
    if isinstance (num,int) and (num>=0) :
        return palindromo_aux(str(num))
    else : return "error de validacion"
def palindromo_aux(cadena):
    if cadena == '' or len (cadena) == 1 :
        return True
    elif cadena[0] == cadena[-1]:
        return palindromo_aux(cadena[1:-1])
    else : return False 
