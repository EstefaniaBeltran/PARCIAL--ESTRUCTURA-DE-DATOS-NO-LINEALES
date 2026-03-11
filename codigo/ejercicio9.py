from typing import List


class EntradaDiccionario:

    def __init__(self, palabra: str, significado: str) -> None:
        self.palabra = palabra
        self.significado = significado


class Diccionario:

    def __init__(self) -> None:
        self.entradas: List[EntradaDiccionario] = []

    def agregar(self, palabra: str, significado: str) -> None:

        self.entradas.append(EntradaDiccionario(palabra, significado))

    def buscar(self, palabra: str) -> str | None:

        for entrada in self.entradas:
            if entrada.palabra == palabra:
                return entrada.significado

        return None


def ejemplo_diccionario():

    dic = Diccionario()

    dic.agregar("casa", "objeto")
    dic.agregar("cat", "animal")

    print(dic.buscar("casa"))