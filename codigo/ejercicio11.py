from typing import List, Tuple, Optional, Iterator


class HashTable:
    """
    Implementación simple de una tabla hash para almacenar
    registros de estudiantes usando su ID como clave.
    """

    def __init__(self, size: int = 10) -> None:
        self.size: int = size
        self.table: List[List[Tuple[int, str]]] = [[] for _ in range(size)]

    def _hash(self, key: int) -> int:
        """Calcula la posición en la tabla usando módulo."""
        return key % self.size

    def insert(self, key: int, value: str) -> None:
        """Inserta un estudiante en la tabla."""
        index = self._hash(key)
        self.table[index].append((key, value))

    def search(self, key: int) -> Optional[str]:
        """Busca un estudiante por su ID."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def __iter__(self) -> Iterator[Tuple[int, str]]:
        """Permite recorrer todos los elementos almacenados."""
        for bucket in self.table:
            for item in bucket:
                yield item


# Ejemplo
tabla = HashTable()

tabla.insert(101, "Ana")
tabla.insert(102, "Luis")
tabla.insert(103, "Carlos")

print(tabla.search(102))

for estudiante in tabla:
    print(estudiante)

