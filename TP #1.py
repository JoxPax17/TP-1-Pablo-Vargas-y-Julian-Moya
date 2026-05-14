#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 14-05-26 12:41 am
#Version: 3.14.3
import funciones
listaTokens=[]
def menu(listaTokens):
    listaConteos=[]
    listaBitacora= funciones.cargarBitacora()
    totalPalabras = 0
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
        opcion=int(input("Escoja una opción: "))
        if opcion>=0 and opcion<=9:
            if opcion==1:
                listaTokens= funciones.cargarArchivoTokens(listaTokens)
            elif opcion==2 :
                funciones.mostrarTokens(listaTokens)
            elif opcion==3:
                listaTokens= funciones.agregarOModificarTokens(listaTokens)
            elif opcion==4:
                funciones.guardarTokensEnArchivo(listaTokens)
            elif opcion==5:
                listaConteos,totalPalabras= funciones.traducirCodigo(listaTokens)
            elif opcion==6:
                funciones.generarCSV(listaConteos)  
            elif opcion==7: 
                funciones.generarHTML(listaConteos,totalPalabras)
            elif opcion==8:
                funciones.submenuBitacora(listaBitacora)
            elif opcion==9: 
                break
        else:
            print ("\nOpcion invalida\n")

#Programa principal
listaTokens=[]
menu(listaTokens)
