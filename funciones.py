#Elaborado por: Pablo Vargas y Julian Moya
#Fecha de creación: 01-05-26 10:00 am
#Ultima modificacio: 01-05-26 11:00 pm
#Version: 3.14.3

#Definicion de funciones:
def crearListaPrueba():
    listaDeTuplas = []
    listaDeTuplas.append(("def", "FUNCION"))
    listaDeTuplas.append(("if", "SI"))
    listaDeTuplas.append(("return", "RETORNAR"))
    return listaDeTuplas  
def mostrarTokens (listaDeTuplas):
    if len(listaDeTuplas)>0:
        print ("--- Tokens cargados ---")
        for tupla in listaDeTuplas:
            palabra=tupla[0]
            token=tupla[1]
            print ("\n",palabra," es ahora ",token,"\n")
    else:
        print ("--- No hay tokens cargados ---")
