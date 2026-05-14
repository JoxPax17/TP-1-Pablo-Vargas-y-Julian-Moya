#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 13-05-26 03:30 pm
#Version: 3.14.3
import funciones
def menu(listaTokens):
    listaConteos = []
    totalPalabras = 0
    duracion = "0 segundos"
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cargar tokens")
        print("2. Mostrar tokens")
        print("3. Agregar/modificar token")
        print("4. Guardar tokens")
        print("5. Traducir código")
        print("6. Generar CSV")
        print("7. Generar HTML")
        print("8. Submenú de bitácora del sistema")
        print("9. Salir\n")
        try:
            opcion = int(input("Escoja una opcion: "))
        except:
            print("Opcion invalida")
        if opcion == 1:
            listaTokens = funciones.cargarArchivoTokens(listaTokens)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se cargaron tokens desde archivo")
        elif opcion == 2:
            funciones.mostrarTokens(listaTokens)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se mostraron los tokens")
        elif opcion == 3:
            listaTokens = funciones.agregarOModificarTokens(listaTokens)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se agregaron/modificaron tokens")
        elif opcion == 4:
            funciones.guardarTokensEnArchivo(listaTokens)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se guardaron tokens en archivo")
        elif opcion == 5:
            inicio = time.time()
            listaConteos, totalPalabras = funciones.traducirCodigo(listaTokens)
            fin = time.time()
            duracion = str(round(fin - inicio, 2)) + " segundos"
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se tradujo un archivo de codigo")
        elif opcion == 6:
            funciones.generarCSV(listaConteos)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se genero reporte CSV")
        elif opcion == 7:
            funciones.generarHTML(listaConteos, duracion, totalPalabras)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se genero reporte HTML")
        elif opcion == 8:
            funciones.submenuBitacora(listaBitacora)
            listaBitacora = funciones.registrarEvento(listaBitacora,"Se ingreso al submenu de bitacora")
        elif opcion == 9:
            listaBitacora = funciones.registrarEvento(listaBitacora,"El usuario salio del programa")
            print("Programa finalizado")
            break
        else:
            print("Opcion invalida")

#Programa principal
listaTokens=[]
menu(listaTokens)
