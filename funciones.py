#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 012-05-26 11:51 pm
#Version: 3.14.3

#Definicion de funciones:
import re
def buscarToken (listaTokens, clavePython):
    """
    Funcionalidad: Busca si una clave de Python ya existe en la lista de tokens y devuelve su posición.
    Entrada: listaTokens (lista de tuplas), clavePython (str)
    Salidas: Índice de la clave encontrada, si -1 es que no esta en la lista (int),
    """
    indice = -1 #Inicializamos para asumir que no esta en la lista
    i = 0
    while i < len(listaTokens) and indice == -1:
        if listaTokens[i][0]==clavePython:
            indice = i   #Se encuentra y se guarda en que posicion esta
        i=i+1
    return indice   #Devuelve la posicion
    
def dividirLinea(linea, separador):
    """
    Funcionalidad: Divide una línea de texto en clave y token usando un separador, validando que ambas partes sean correctas.
    Entrada: linea (str), separador (str)
    Salidas: (clavePython, token) (tupla de str)
    """ 
    partes = linea.strip().split(separador) #divide una linea usando el separador indicado
    if len(partes) != 2: #verifica que la linea haya quedado de dos partes la clave de python y el token 
        return ()
    clavePython = partes[0].strip()   #Quita espacios al inicio y al final
    token = partes[1].strip() 
    if clavePython == "" or token == "":
        return ()#verifica si alguna de las dos partes quedo vacia ya que si no la linea esta incompleta
    return (clavePython, token)

def cargarArchivoTokens(listaTokens):
    """
    Funcionalidad: Carga tokens desde un archivo de texto, agregando nuevos, sobrescribiendo existentes o ignorando líneas inválidas.
    Entrada: listaTokens (lista de tuplas), nombreArchivo (str), separador (str)
    Salidas: verifica, listaTokens actualizada (lista de tuplas)
    """
    nombreArchivo = input("  Nombre del archivo con su respectiva extension: ").strip()
    separador = input("  Indique el separador usado en el archivo ejemplo -> ,=: ").strip()
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
                if len(par) == 0:
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
        print("Error, el archivo no existe, no se pudo abrir o el separador fue ingresado incorrectamente, intente de nuevo")
        return listaTokens 
    return listaTokens
    
def mostrarTokens (listaTokens):
    """
    Funcionalidad: Muestra los tokens cargados o indica que no hay ninguno
    Entrada: listaTokens (lista de tuplas)
    Salidas: pretty print
    """
    if len(listaTokens)>0:
        print ("--- Tokens cargados ---")
        for tupla in listaTokens:
            palabra=tupla[0]
            token=tupla[1]
            print ("\n",palabra," es ahora ",token,"\n")
    else:
        print ("--- No hay tokens cargados ---")
    return

def agregarOModificarTokens(listaTokens):
    """
    Funcionalidad: Permite agregar tokens nuevos o actualizar existentes
    Entrada: listaTokens (lista de tuplas)
    Salida: listaTokens (lista de tuplas)
    """
    print("\n--- Agregar o modificar tokens ---")
    print("Digite 0 para salir sin cambios.")
    print("Ingrese varios pares con la clave de python y el token, cada par separelo con una coma.")
    print("Ejemplo con el separador ->: def->funcion,while->mientras")
    entrada = input("Ingrese los tokens: ").strip()
    if entrada==0:
        print("Operacion cancelada.")
        return listaTokens
    separador = input("Indique el separador usado entre clave y token (ej: ->, =): ").strip()
    if separador == "":
        print("El separador no puede estar vacio.")
        return listaTokens
    pares = entrada.split(",")
    for i in range(len(pares)):
        par = dividirLinea(pares[i], separador)
        if len(par) == 0:
            print("El par '" + pares[i].strip() + "' estaba mal escrito, se ignoro.")
        else:
            clavePython = par[0]
            token = par[1]
            indice = buscarToken(listaTokens, clavePython)
            if indice != -1:
                listaTokens[indice] = (clavePython, token)
                print("Actualizacion: '" + clavePython + "' ahora es '" + token + "'")
            else:
                listaTokens.append((clavePython, token))
                print("Añadido: '" + clavePython + "' -> '" + token + "'")
    return listaTokens

def guardarTokensEnArchivo(listaTokens):
    """
    Funcionalidad: Guarda los tokens actuales en un archivo de texto nuevo
    Entrada: listaTokens (lista de tuplas)
    Salida: ninguna
    """
    print("\n--- Guardar tokens en archivo ---")
    if len(listaTokens) == 0:
        print("No hay tokens en memoria para guardar.")
        return
    nombreArchivo = input("Nombre del archivo de salida: ").strip()
    if nombreArchivo == "":
        print("El nombre no puede estar vacio.")
        return
    separador = input("Separador a usar entre clave y token (ej: ->, ,, =): ").strip()
    if separador == "":
        print("El separador no puede estar vacio.")
        return
    try:
        archivo = open(nombreArchivo, "w") #el w abre el archivo en modo de escritura
        for i in range(len(listaTokens)):
            clavePython = listaTokens[i][0]
            token = listaTokens[i][1]
            archivo.write(clavePython + separador + token + "\n")
        archivo.close()
        print("Tokens guardados correctamente en '" + nombreArchivo + "'.")
    except:
        print("Error, no se pudo guardar el archivo.")

def esNumero(texto):
    """
    Funcionalidad: Verifica si un texto es un numero
    Entrada: texto (str)
    Salida: True si es numero, False si no
    """
    esNum=True
    if re.match(texto,"^\D$"):
        return True
    return False

def extraerPalabras(linea):
    """
    Funcionalidad: Separa una linea en palabras y caracteres especiales
    Entrada: linea (str)
    Salida: lista con las partes de la linea
    """
    partes = []
    palabraActual = ""
    caracteresEspeciales = " ()[]:,=+-*/<>!\"'\n\t"
    for i in range(len(linea)):
        caracter = linea[i]
        if caracter in caracteresEspeciales:
            if palabraActual != "": #Si esta vacia empezamos a añadir
                partes.append(palabraActual)
                palabraActual = "" 
            partes.append(caracter) #El caracter especial se guarda asi como esta
        else:
            palabraActual = palabraActual + caracter #Si es parte de una palabra, la seguimos acumulando
    if palabraActual != "":
        partes.append(palabraActual) #Si quedo una palabra al final la guardamos
    return partes

def traducirCodigo(listaTokens):
    """
    Funcionalidad: Lee un archivo de codigo Python y reemplaza las
    claves de Python por sus tokens, guardando el resultado en otro archivo
    Entrada: listaTokens (lista de tuplas)
    Salida: ninguna
    """
    print("\n--- Traducir codigo ---")
    if len(listaTokens)==0:
        print("No hay tokens cargados. Cargue tokens primero.")
        return
    nombreEntrada = input("Nombre del archivo a traducir ej: codigo.py: ").strip()
    nombreSalida = input("Nombre del archivo de salida ej: traducido.py: ").strip()
    if nombreEntrada == "" or nombreSalida == "":
        print("Los nombres no pueden estar vacios.")
        return
    try:
        archivoEntrada = open(nombreEntrada, "r")
        lineas = archivoEntrada.readlines()
        archivoEntrada.close()
    except:
        print("Error, el archivo no existe o no se pudo abrir.")
        return
    try:
        archivoSalida = open(nombreSalida, "w")
        for i in range(len(lineas)):
            linea = lineas[i]
            partes = extraerPalabras(linea)
            lineaNueva = ""
            for j in range(len(partes)):
                parte = partes[j]
                if len(parte)==1 and parte in " ()[]:,=+-*/<>!\"'\n\t":
                    lineaNueva=lineaNueva+parte #Si es numero o caracter especial lo dejamos igual
                elif esNumero(parte):
                    lineaNueva=lineaNueva+parte
                else:
                    indice = buscarToken(listaTokens, parte) #Buscamos si la palabra esta en listaTokens =-1 entonces la dejamos igual
                    if indice != -1: #La funcion buscarToken devuelve -1 si la palabra esta en listaTokens, indice !=-1, entonces la cambiamos por el token
                        lineaNueva=lineaNueva+listaTokens[indice][1]
                    else: #si indice =-1 la dejamos igual
                        lineaNueva=lineaNueva+parte
            archivoSalida.write(lineaNueva)
        archivoSalida.close()
        print("Archivo traducido guardado como '" + nombreSalida + "'.")

#Programa Principal
listaTokens = []
listaTokens = cargarArchivoTokens(listaTokens)
mostrarTokens(listaTokens)
