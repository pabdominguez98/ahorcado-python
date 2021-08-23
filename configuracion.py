
def leer_linea(archivo):
    """
    Esta funcion lee la una linea del archivo csv, y devuelve una lista con
    los valores de esa linea.

    Autor:...
    """
    linea = archivo.readline()
    lista_linea = linea.rstrip('\n').split(',')
    
    return lista_linea
    

def configuracion():
    """
    Se toman los datos del archivo csv y se devuelve una lista con los valores numéricos 
    que se encunetran en el mismos.

    Autor:...
    """
    archivo_abierto = open("configuracion.csv")
    lista_linea = leer_linea(archivo_abierto)
    valores = []
    while lista_linea != [''] :
        valor = lista_linea[1]
        valores.append(int(valor))
        lista_linea = leer_linea(archivo_abierto)
        
    
    return valores
    




