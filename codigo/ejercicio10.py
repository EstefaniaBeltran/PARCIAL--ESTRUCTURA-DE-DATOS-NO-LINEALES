from typing import List


class NodoBusqueda:

    def __init__(self, termino: str) -> None:
        self.termino = termino
        self.relacionados: List["NodoBusqueda"] = []


class MotorBusqueda:

    def __init__(self) -> None:
        self.indices: List[NodoBusqueda] = []

    def agregar(self, termino: str) -> NodoBusqueda:

        nodo = NodoBusqueda(termino)
        self.indices.append(nodo)

        return nodo


def ejemplo_busqueda():

    motor = MotorBusqueda()

    CCIA = motor.agregar("CCIA")
    negocios = motor.agregar("negocios")

    CCIA.relacionados.append(negocios)

    print(CCIA.termino)