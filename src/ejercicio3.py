"""Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla generica de tal modo que pueda aceptar una cadena y una letra como argumentos."""

def cuenta(cadena, letra):
    #Inicializamos un contador para llevar la cuenta de la letra
    contador = 0
    
    #Iteramos sobre cada caracter en la cadena
    for caracter in cadena:
        #Comparamos el caracter actual con la letra que estamos contando
        if caracter == letra:
            #Si son iguales, incrementamos el contador
            contador += 1
    
    #Devolvemos el valor del contador
    return contador

if __name__ == "__main__":

    #Llamamos a la funcion cuenta con la cadena 'banana' y la letra 'a'
    resultado = cuenta('banana', 'a')
    
    #Imprimimos el resultado, que indica cuantas veces aparece 'a' en 'banana'
    print(resultado)