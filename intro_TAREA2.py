def formar(num):
    if isinstance (num,int):
        return formar_aux(num)
    else : return "Error de valadacion"
def formar_aux(num):
    if num == 0:
        return []
    elif num%10%2==0:
        return ([num%10] + formar_aux(num//10))
    else : return formar_aux(num//10)
