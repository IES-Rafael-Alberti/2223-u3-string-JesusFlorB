"""Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, 
imprimiendo cada letra en una línea independiente."""

def imprimir_inverso(cadena):
    #Obtenemos la longitud de la cadena
    longitud = len(cadena)
    #Inicializamos el indice en el ultimo caracter
    indice = longitud - 1
    resultado = ""  #Creamos una cadena vacia para almacenar el resultado invertido

    while indice >= 0:
        #Concatenamos el caracter en la posicion del indice actual al resultado
        resultado += cadena[indice]
        #Decrementamos el indice para movernos hacia atras en la cadena
        indice -= 1

    return resultado  #Devolvemos la cadena invertida

if __name__ == "__main__":


    cadena = input("Escribe una frase: ")
    #Llamamos a la funcion para imprimir la cadena al reves
    resultado = imprimir_inverso(cadena)
    print(resultado)  #Imprimimos el resultado invertido en la consola