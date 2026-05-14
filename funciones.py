#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 14-05-26 12:41 am
#Version: 3.14.3

#Definicion de funciones:
import re
import datetime
import pickle
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
    nombreArchivo = input("Nombre del archivo con su respectiva extension: ").strip()
    separador = input("Indique el separador usado en el archivo ejemplo ->,=: ").strip()
    if separador == "":
        print("El separador no puede ser vacio.")
        return listaTokens
    try:
        archivo=open(nombreArchivo, "r") #Abrir el archivo para lectura
        lineas=archivo.readlines() #para leer todas las linea de una vez
        archivo.close()
        ignorados=0
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
                    else:
                        listaTokens.append((clavePython, token))
    except:
        print("Error, el archivo no existe, no se pudo abrir o el separador fue ingresado incorrectamente, intente de nuevo")
        return listaTokens 
    return listaTokens   

def mostrarTokens(listaTokens):
    """
    Funcionalidad: Muestra los tokens cargados o indica que no hay ninguno
    Entrada: listaTokens (lista de tuplas)
    Salidas: pretty print
    """
    if len(listaTokens) > 0:
        print("\n--- Tokens cargados ---\n---------------------------")
        for tupla in listaTokens:
            palabra = tupla[0]
            token = tupla[1]
            print("  " + palabra + " es ahora: " + token)
        print("---------------------------\n--- Total: " + str(len(listaTokens)) + " token(s) ---\n")
    else:
        print("\n--- No hay tokens cargados ---\n")
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
    if entrada=="0":
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
    if re.match("^\\d+$", texto):
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
    Funcionalidad: Lee un archivo de codigo Python y reemplaza las claves por sus tokens.
    Entrada: listaTokens (lista de tuplas)
    Salida: validaciones, listaConteos (lista de tuplas con clave, token y cantidad de reemplazos) totalPalabras (int) cantidad total de palabras procesadas.
    """
    print("\nTraducir codigo")
    if len(listaTokens) == 0:
        print("No hay tokens cargados. Cargue tokens primero.")
        return [], 0
    nombreEntrada = input("Nombre del archivo a traducir ej: codigo.py: ").strip()
    nombreSalida  = input("Nombre del archivo de salida ej: traducido.py: ").strip()
    if nombreEntrada == "" or nombreSalida == "":
        print("Los nombres no pueden estar vacios.")
        return [], 0
    try:
        archivoEntrada = open(nombreEntrada, "r")
        lineas = archivoEntrada.readlines()
        archivoEntrada.close()
    except:
        print("Error, el archivo no existe o no se pudo abrir.")
        return [], 0
    listaConteos = [] #Inicializamos listaConteos con conteo 0 para cada token
    for i in range(len(listaTokens)):
        listaConteos.append((listaTokens[i][0], listaTokens[i][1], 0))
    totalPalabras = 0 # totalPalabras cuenta todas las palabras procesadas (sin contar numeros ni caracteres especiales)
    try:
        archivoSalida = open(nombreSalida, "w")
        for i in range(len(lineas)):
            linea = lineas[i] #Lineas archivo de entrada
            partes = extraerPalabras(linea)
            lineaNueva = ""
            for j in range(len(partes)):
                parte = partes[j]
                if len(parte) == 1 and parte in " ()[]:,=+-*/<>!\"'\n\t":
                    lineaNueva = lineaNueva + parte #Es caracter especial entonces se deja igual
                elif esNumero(parte):
                    lineaNueva = lineaNueva + parte #Es numero entonces se deja igual
                else:
                    totalPalabras+= 1 # Es una palabra, la contamos
                    indice = buscarToken(listaTokens, parte) #Buscamos si la palabra esta en listaTokens
                    if indice != -1: #La funcion buscarToken devuelve -1 si la palabra no esta en listaTokens, entonces si indice !=-1, entonces la cambiamos por el token correspondiente
                        lineaNueva = lineaNueva + listaTokens[indice][1] #La palabra esta en listaTokens, la reemplazamos
                        conteoActual = listaConteos[indice][2] #Actualizamos el conteo sumandole 1
                        listaConteos[indice] = (listaConteos[indice][0], listaConteos[indice][1], conteoActual + 1)
                    else:
                        lineaNueva=lineaNueva+parte #La palabra no esta en listaTokens, la dejamos igual
            archivoSalida.write(lineaNueva)
        archivoSalida.close()
        print("Archivo traducido guardado como '" + nombreSalida + "'.")
    except:
        print("Error, no se pudo escribir el archivo de salida.")
        return [], 0
    return listaConteos, totalPalabras

def generarCSV(listaConteos):
    """
    Funcionalidad: Genera un archivo CSV con la palabra original, su token y cantidad de reemplazos.
    Entrada: listaConteos (lista de tuplas con clave, token y conteo)
    Salida: validaciones, reportes.
    """
    print("\nGenerar reporte CSV")
    if len(listaConteos) == 0:
        print("No hay reemplazos para reportar. Traduzca un archivo primero.")
        return
    nombreArchivo = input("Nombre del archivo CSV de salida (ej: reporte.csv): ").strip()
    if nombreArchivo == "":
        print("El nombre no puede estar vacio.")
        return
    try:
        archivo = open(nombreArchivo, "w")
        archivo.write("Palabra original,Token de reemplazo,Cantidad de reemplazos\n") #encabezado de las columnas
        for i in range(len(listaConteos)):
            clavePython=listaConteos[i][0]
            token=listaConteos[i][1]
            conteo=listaConteos[i][2]
            archivo.write(clavePython + "," + token + "," + str(conteo) + "\n")
        archivo.close()
        print("Reporte CSV guardado como: " + nombreArchivo)
    except:
        print("Error, no se pudo generar el archivo CSV.")

def obtenerFecha():
    ahora   = datetime.datetime.now()
    anno    = str(ahora.year)
    mes     = str(ahora.month).zfill(2) #el z.fill se asegura que algo tenga x digitos, por ejemplo un 5 pasa a un 05
    dia     = str(ahora.day).zfill(2)
    hora    = str(ahora.hour).zfill(2)
    minuto  = str(ahora.minute).zfill(2)
    segundo = str(ahora.second).zfill(2)
    return anno + "-" + mes + "-" + dia + "_" + hora + ":" + minuto + ":" + segundo

def generarHTML(listaConteos, totalPalabras):
    """
    Funcionalidad: Genera un reporte HTML con los resultados de la traduccion
    Entrada: listaConteos (lista de tuplas), duracion (str), totalPalabras (int)
    Salida: archivo HTML generado
    """
    if len(listaConteos) == 0:
        print("No hay reemplazos para reportar. Traduzca un archivo primero.")
        return
    fechaTexto = obtenerFecha()
    nombreArchivo = "reporteHTML_" + fechaTexto.replace(":", "-").replace("_", "-") + ".html"
    titulo = input("Ingrese el titulo del reporte: ").strip()
    if titulo == "":
        titulo = "Reporte de Traduccion"
    totalReemplazos = 0
    for i in range(len(listaConteos)):
        totalReemplazos = totalReemplazos + listaConteos[i][2]
    if totalPalabras > 0:
        porcentaje = str(round((totalReemplazos * 100) / totalPalabras, 2))
    else:
        porcentaje = "0"
    try:
        archivo = open(nombreArchivo, "w")
        archivo.write("<html>\n")
        archivo.write("<head>\n")
        archivo.write("<title>" + titulo + "</title>\n")
        archivo.write("</head>\n")
        archivo.write("<body>\n")
        archivo.write("<h1>Reporte de Traduccion</h1>\n")
        archivo.write("<h2>" + fechaTexto + "</h2>\n")
        archivo.write("<p>Total de reemplazos: " + str(totalReemplazos) + "</p>\n")
        archivo.write("<p>Porcentaje de palabras reemplazadas: " + porcentaje + "%</p>\n")
        archivo.write("<table border='1'>\n")
        archivo.write("<tr><th>Palabra</th><th>Token</th><th>Reemplazos</th></tr>\n")
        for i in range(len(listaConteos)):
            if i % 2 == 0:
                color = "#ffffff"
            else:
                color = "#cccccc"
            archivo.write("<tr bgcolor='" + color + "'>")
            archivo.write("<td align='center'>" + listaConteos[i][0] + "</td>")
            archivo.write("<td align='center'>" + listaConteos[i][1] + "</td>")
            archivo.write("<td align='center'>" + str(listaConteos[i][2]) + "</td>")
            archivo.write("</tr>\n")
        archivo.write("</table>\n")
        archivo.write("</body>\n")
        archivo.write("</html>\n")
        archivo.close()
        print("Reporte HTML generado como '" + nombreArchivo + "'.")
    except:
        print("Error, no se pudo generar el archivo HTML.")

def registrarEvento(listaBitacora, descripcion):
    """
    Funcionalidad: Agrega un nuevo evento a la bitacora en memoria
    y lo guarda de inmediato en el archivo binario bitacora.txt
    Entrada: listaBitacora (lista de tuplas), descripcion (str)
    Salida: listaBitacora actualizada
    """
    registro = (obtenerFecha(), descripcion)
    listaBitacora.append(registro) #La agregamos a la lista en memoria
    try:
        archivo = open("bitacora.txt", "wb") #La guardamos de inmediato en el archivo binario, wb para escribir en archivo binario
        pickle.dump(listaBitacora, archivo) #dump = metodo para grabar
        archivo.close()
    except:
        print("Error, no se pudo guardar la bitacora en disco.")
    return listaBitacora
 
def cargarBitacora():
    """
    Funcionalidad: Carga la bitacora desde el archivo binario al iniciar el programa.
    Si el archivo no existe, la bitacora empieza vacia.
    Entrada: ninguna
    Salida: listaBitacora (lista de tuplas)
    """
    listaBitacora = []
    try:
        archivo = open("bitacora.txt", "rb") #rb para leer un archivo binario
        listaBitacora = pickle.load(archivo) #se lee un valor del archivo
        archivo.close()
    except:
        listaBitacora = [] #si el archivo no existe se arranca con lista vacia
    return listaBitacora
  
def filtrarPorFecha(listaBitacora):
    """
    Funcionalidad: Muestra los registros de la bitacora de un dia especifico
    Entrada: listaBitacora (lista de tuplas)
    Salida: ninguna
    """
    print("\nBitacora: filtrar por fecha")
    fecha=input("Ingrese la fecha a buscar con el siguiente formato AAAA-MM-DD: ").strip()
    if fecha == "":
        print("Debe ingresar una fecha.")
        return
    print("\nResultados para la fecha: " + fecha + "\n")
    encontrados = 0
    for i in range(len(listaBitacora)):
        #El tiempo lo da con el formato: "AAAA-MM-DD_hh:mm:ss", tomamos solo los primeros 10 caracteres que son la fecha
        fechaRegistro = listaBitacora[i][0][:10]
        if fechaRegistro==fecha:
            print(listaBitacora[i][0] + "  |  " + listaBitacora[i][1])
            encontrados+= 1
    if encontrados == 0:
        print("No se encontraron registros para esa fecha.")
    else:
        print("\nTotal encontrados: ", encontrados)
 
def filtrarPorPalabraClave(listaBitacora):
    """
    Funcionalidad: Muestra los registros cuya descripcion contiene una palabra clave
    Entrada: listaBitacora (lista de tuplas)
    Salida: ninguna
    """
    print("\nBitacora: filtrar por palabra clave")
    palabras = input("Ingrese palabras clave separadas por coma: ").strip()
    if palabras == "":
        print("Debe ingresar al menos una palabra clave.")
        return
    listaPalabras = palabras.split(",") #Separamos las palabras clave por coma
    for i in range(len(listaPalabras)):
        listaPalabras[i] = listaPalabras[i].strip().lower() #Limpiamos espacios de cada palabra y la ponemos en minuscula
    print("\nResultados:")
    encontrados = 0
    for i in range(len(listaBitacora)):
        descripcion=listaBitacora[i][1].lower()
        for j in range(len(listaPalabras)):
            if listaPalabras[j] in descripcion: #Para ver si alguna de las palabras clave esta en la descripcion
                print(listaBitacora[i][0] + "  |  " + listaBitacora[i][1])
                encontrados = encontrados + 1
                break  # Para no imprimir el mismo registro dos veces
    if encontrados == 0:
        print("No se encontraron registros con esas palabras clave.\n")
    else:
        print("Total encontrados: " + str(encontrados))
 
def submenuBitacora(listaBitacora):
    """
    Funcionalidad: Submenu para consultar la bitacora del sistema
    Entrada: listaBitacora (lista de tuplas)
    Salida: ninguna
    """
    salir = False
    while salir==False:
        print("\nSubmenu de bitacora")
        print("A) Acciones por dia escogido")
        print("B) Acciones con palabras clave")
        print("C) Salir del submenu")
        opcion = input("Seleccione una opcion: ").strip().upper()
        if opcion == "A":
            filtrarPorFecha(listaBitacora)
        elif opcion == "B":
            filtrarPorPalabraClave(listaBitacora)
        elif opcion == "C":
            salir = True
        else:
            print("Opcion invalida.")
