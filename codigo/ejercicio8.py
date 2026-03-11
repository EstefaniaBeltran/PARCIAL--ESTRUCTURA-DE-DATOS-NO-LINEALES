from typing import Optional


class NodoDecision:

    def __init__(self, pregunta: str) -> None:
        self.pregunta = pregunta
        self.si: Optional["NodoDecision"] = None
        self.no: Optional["NodoDecision"] = None


class ArbolDecision:

    def __init__(self, raiz: NodoDecision) -> None:
        self.raiz = raiz


def ejemplo_decision():

    raiz = NodoDecision("¿Está lloviendo?")

    raiz.si = NodoDecision("Llevar paraguas")
    raiz.no = NodoDecision("No llevar paraguas")

    arbol = ArbolDecision(raiz)

    print(arbol.raiz.pregunta)