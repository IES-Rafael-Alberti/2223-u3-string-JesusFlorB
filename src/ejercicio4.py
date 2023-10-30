"""Hay un método de cadenas llamado count que es similar a find. Escribe el código necesario para invocar a este método 
y contar el número de veces que una letra aparece en “banana”."""

def contar_letras(cadena, letra):
    #Usamos count para contar cuantas veces aparece 'letra' en 'cadena'
    contador = cadena.count(letra)
    return contador

if __name__ == "__main__":


    #Definimos la cadena y la letra a contar
    cadena = "banana"
    letra = "a"

    #Llamamos a la funcion contar_letras y almacenamos el resultado
    contador = contar_letras(cadena, letra)

    #Imprimimos el resultado
    print(contador)