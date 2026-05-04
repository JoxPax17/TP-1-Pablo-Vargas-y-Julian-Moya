#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 01-05-26 11:00 pm
#Version: 3.14.3

#Definicion de funciones:
def buscarToken ():

def dividirLinea(linea, separador):
    partes = linea.strip().split(separador) #divide una linea usando el separador indicado
    if len(partes) != 2: #verifica que la linea haya quedado de dos partes la clave de python y el token 
        return
    clavePython = partes[0].strip()   #Quita espacios al inicio y al final
    token = partes[1].strip() 
    if clavePython == "" or token == "":
        return #verifica si alguna de las dos partes quedo vacia ya que si no la linea esta incompleta
    return (clavePython, token)

def cargarArchivoTokens(listaTokens):
    nombreArchivo = input("  Nombre del archivo con su respectiva extension: ").strip()
    separador = input("  Indique el separador usado en el archivo ejemplo: ""->"" "","" ""=""").strip()
    if separador == "":
        print("El separador no puede ser vacio.")
        return listaTokens
    cargados   = 0
    reescritos = 0
    ignorados  = 0  #estas tres variables son contadores para un resumen al final
    try:
        archivo=open(nombreArchivo, "r") #Abrir el archivo para lectura
        lineas=archivo.readlines() #para leer todas las linea de una vez
        archivo.close()
        for i in range(len(lineas)):
            linea = lineas[i]
            if linea.strip() != "": #Si la linea esta vacia la salta
                par = dividirLinea(linea, separador) #divide una linea en (clavePython, token)
                if par == None:
                    print("La linea " + str(i + 1) + "se ignoro ya que estaba mal escrita: " + linea.strip())
                    ignorados = ignorados + 1 #Si dividirLinea devolvio None, la linea estaba mal escrita
                else:
                    clavePython=par[0]
                    token=par[1]
                    indice= buscarToken (listaTokens, clavePython) #Busca si la clave de python ya esta sobreescrita en la lista
                    if indice != -1:
                        listaTokens[indice]=(clavePython, token)
                        print ("La palabra reservada de python: ", clavePython ,"ahora se sustituyo por el token: ", token)
                        reescritos+=1
                    else:
                        listaTokens.append((clavePython, token))
                        cargados+=1
    except:
        print("Error, el archivo no existe o no se pudo abrir, intente de nuevo")
        return listaTokens 
    return listaTokens
def mostrarTokens (listaTokens):
    if len(listaTokens)>0:
        print ("--- Tokens cargados ---")
        for tupla in listaTokens:
            palabra=tupla[0]
            token=tupla[1]
            print ("\n",palabra," es ahora ",token,"\n")
    else:
        print ("--- No hay tokens cargados ---")
