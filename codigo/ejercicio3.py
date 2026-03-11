from typing import List, Generator


class Persona:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.hijos: List["Persona"] = []

    def agregar_hijo(self, hijo: "Persona") -> None:
        self.hijos.append(hijo)

    def recorrer(self) -> Generator[str, None, None]:
        yield self.nombre
        for hijo in self.hijos:
            yield from hijo.recorrer()


class ArbolGenealogico:

    def __init__(self, raiz: Persona) -> None:
        self.raiz = raiz

    def recorrer(self) -> Generator[str, None, None]:
        yield from self.raiz.recorrer()


def ejemplo_familia() -> ArbolGenealogico:

    abuelo = Persona("Abuelo")

    padre = Persona("Padre")
    tia = Persona("Tia")

    padre.agregar_hijo(Persona("Hijo1"))
    padre.agregar_hijo(Persona("Hijo2"))

    tia.agregar_hijo(Persona("Primo1"))

    abuelo.agregar_hijo(padre)
    abuelo.agregar_hijo(tia)

    return ArbolGenealogico(abuelo)


if __name__ == "__main__":

    familia = ejemplo_familia()

    for persona in familia.recorrer():
        print(persona)