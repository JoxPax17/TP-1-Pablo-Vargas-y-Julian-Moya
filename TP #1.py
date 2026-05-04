#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 03-05-26 11:00 pm
#Version: 3.14.3
import funciones
def menu():
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
                opcion1()
            elif opcion==2 :
                opcion1()
            elif opcion==3:
                opcion1()
            elif opcion==4:
                opcion1()
            elif opcion==5:
                opcion1()
            elif opcion==6:
                opcion1()   
            elif opcion==7: 
                opcion1()
            elif opcion==8:
                while True:
                    print ("\nA. Acciones por dia escogido")
                    print ("B. Acciones con algunas palabras clave")
                    print ("C. Salir del submenu\n")
                    opcion=str(input("Escoja una opción: "))
                    if opcion=="A" or opcion=="a":
                        opcion1()
                    elif opcion=="B" or opcion=="b":
                        opcion1()
                    elif opcion=="C" or opcion=="c":
                        break 
                    else:
                        print ("\nOpcion invalida\n")
            elif opcion==9: 
                break
        else:
            print ("\nOpcion invalida\n")
        menu()

#Programa principal
menu()
