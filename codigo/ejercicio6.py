from typing import Dict


class NodoTrie:
    """
    Nodo de un Trie.
    """

    def __init__(self) -> None:
        self.hijos: Dict[str, "NodoTrie"] = {}
        self.fin_palabra: bool = False


class Trie:
    """
    Implementación de un Trie.
    """

    def __init__(self) -> None:
        self.raiz = NodoTrie()

    def insertar(self, palabra: str) -> None:

        nodo = self.raiz

        for letra in palabra:

            if letra not in nodo.hijos:
                nodo.hijos[letra] = NodoTrie()

            nodo = nodo.hijos[letra]

        nodo.fin_palabra = True

    def buscar(self, palabra: str) -> bool:

        nodo = self.raiz

        for letra in palabra:

            if letra not in nodo.hijos:
                return False

            nodo = nodo.hijos[letra]

        return nodo.fin_palabra


def ejemplo_trie():

    trie = Trie()

    trie.insertar("casa")
    trie.insertar("carro")
    trie.insertar("carta")

    print(trie.buscar("casa"))
    print(trie.buscar("carta"))