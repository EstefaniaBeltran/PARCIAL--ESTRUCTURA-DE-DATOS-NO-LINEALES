class CorrectorOrtografico:
    """
    Corrector basado en Trie.
    """

    def __init__(self, trie: Trie) -> None:
        self.trie = trie

    def cargar_palabras(self, palabras: list[str]) -> None:

        for palabra in palabras:
            self.trie.insertar(palabra)

    def verificar(self, palabra: str) -> bool:

        return self.trie.buscar(palabra)


def ejemplo_corrector():

    trie = Trie()
    corrector = CorrectorOrtografico(trie)

    palabras = ["hola", "mundo", "python"]

    corrector.cargar_palabras(palabras)

    print(corrector.verificar("hola"))
    print(corrector.verificar("java"))