from typing import Dict


class TrieNode:
    """Nodo de un Trie."""

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.end: bool = False


class Trie:
    """
    Implementación básica de un Trie para almacenar palabras.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserta una palabra."""
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.end = True

    def search(self, word: str) -> bool:
        """Busca una palabra."""
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.end


# Ejemplo
trie = Trie()

trie.insert("python")
trie.insert("programacion")

print(trie.search("python"))
print(trie.search("java"))