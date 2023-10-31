from src.ejercicio1 import imprimir_inverso

def test_imprimir_inverso():
    assert imprimir_inverso('hola mundo') == 'odnum aloh'
    assert imprimir_inverso('12345') == '54321'
    assert imprimir_inverso('') == ''