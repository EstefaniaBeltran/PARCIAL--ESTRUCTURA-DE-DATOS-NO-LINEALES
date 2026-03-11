from typing import List, Generator


class Nodo:
    """
    Representa un nodo dentro de un árbol N-ario.
    """

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.hijos: List["Nodo"] = []

    def agregar_hijo(self, hijo: "Nodo") -> None:
        """Agrega un nodo hijo."""
        self.hijos.append(hijo)

    def recorrer(self) -> Generator[str, None, None]:
        """Recorre el árbol en profundidad."""
        yield self.nombre
        for hijo in self.hijos:
            yield from hijo.recorrer()


class ArbolNario:
    """
    Representa un árbol N-ario completo.
    """

    def __init__(self, raiz: Nodo) -> None:
        self.raiz = raiz

    def recorrer(self) -> Generator[str, None, None]:
        yield from self.raiz.recorrer()


def ejemplo_universidad() -> ArbolNario:

    rectoria = Nodo("Rectoria")

    ingenieria = Nodo("Facultad Ingenieria")
    derecho = Nodo("Escuela Mayor de Derecho")
    prime = Nodo("PRIME")

    ingenieria.agregar_hijo(Nodo("Ciencia Computacion"))
    ingenieria.agregar_hijo(Nodo("Ingenieria Industrial"))
    ingenieria.agregar_hijo(Nodo("Ingenieria Ambiental"))

    derecho.agregar_hijo(Nodo("Derecho"))
    prime.agregar_hijo(Nodo("Negocios Internacionales"))

    rectoria.agregar_hijo(ingenieria)
    rectoria.agregar_hijo(derecho)
    rectoria.agregar_hijo(prime)

    return ArbolNario(rectoria)


if __name__ == "__main__":

    arbol = ejemplo_universidad()

    print("Recorrido del árbol:")
    for nodo in arbol.recorrer():
        print(nodo)