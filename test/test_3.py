from src.ejercicio3 import cuenta

def test_cuenta():
    assert cuenta('banana', 'a') == 3
    assert cuenta('pelicula', 'l') == 2
    assert cuenta('ornitorrinco', 'a') == 0
    assert cuenta('zzzzz', 'z') == 5