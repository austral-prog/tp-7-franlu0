def enumerate_list(lista):
    x=[]
    for e in lista:
        if e != "":
            x+=  [f"{len (x)}. {e}"]  
    return x

def enumerate_backwards(lista):
    x=[]
    for e in lista:
        if e != "":
            x+=  [f"{len (x)}. {e[::-1]}"]  
    return x
    
