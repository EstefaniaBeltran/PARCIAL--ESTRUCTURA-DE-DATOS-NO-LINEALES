from typing import List, Generator


class NodoArchivo:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.hijos: List["NodoArchivo"] = []

    def agregar(self, nodo: "NodoArchivo") -> None:
        self.hijos.append(nodo)

    def recorrer(self) -> Generator[str, None, None]:
        yield self.nombre
        for h in self.hijos:
            yield from h.recorrer()


class SistemaArchivos:

    def __init__(self, raiz: NodoArchivo) -> None:
        self.raiz = raiz

    def recorrer(self) -> Generator[str, None, None]:
        yield from self.raiz.recorrer()


def ejemplo_sistema_archivos() -> SistemaArchivos:

    Sistema_archivos = NodoArchivo("Sistema_archivos")

    documentos = NodoArchivo("documentos")
    imagenes = NodoArchivo("imagenes")

    documentos.agregar(NodoArchivo("tarea.docx"))
    documentos.agregar(NodoArchivo("tesis.pdf"))

    imagenes.agregar(NodoArchivo("foto1.png"))
    imagenes.agregar(NodoArchivo("foto2.png"))

    Sistema_archivos.agregar(documentos)
    Sistema_archivos.agregar(imagenes)

    return SistemaArchivos(Sistema_archivos)


if __name__ == "__main__":

    sistema = ejemplo_sistema_archivos()

    for archivo in sistema.recorrer():
        print(archivo)