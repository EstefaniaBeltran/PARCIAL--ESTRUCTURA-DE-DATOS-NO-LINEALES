from typing import List


class Modulo:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.dependencias: List["Modulo"] = []

    def agregar_dependencia(self, modulo: "Modulo") -> None:
        self.dependencias.append(modulo)


class SistemaModulos:

    def __init__(self, raiz: Modulo) -> None:
        self.raiz = raiz


def ejemplo_dependencias() -> SistemaModulos:

    sistema = Modulo("Sistema")

    moduloA = Modulo("ModuloA")
    moduloB = Modulo("ModuloB")

    moduloA.agregar_dependencia(Modulo("Libreria1"))
    moduloA.agregar_dependencia(Modulo("Libreria2"))

    moduloB.agregar_dependencia(Modulo("Libreria3"))

    sistema.agregar_dependencia(moduloA)
    sistema.agregar_dependencia(moduloB)

    return SistemaModulos(sistema)