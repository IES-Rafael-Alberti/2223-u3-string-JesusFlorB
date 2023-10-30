from src.ejercicio4 import contar_letras

def test_contar_letras():
    assert contar_letras('banana', 'a') == 3
    assert contar_letras('hola', 'o') == 1
    assert contar_letras('programacion', 'z') == 0
    assert contar_letras('aaaeeeiiiooouuu', 'i') == 3