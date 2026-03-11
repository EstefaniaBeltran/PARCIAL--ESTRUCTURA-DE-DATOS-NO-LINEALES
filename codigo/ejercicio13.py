import heapq
from typing import List, Iterator


class MinHeap:
    """
    Implementación de un heap mínimo usando heapq.
    """

    def __init__(self) -> None:
        self.heap: List[int] = []

    def insert(self, value: int) -> None:
        """Inserta un elemento en el heap."""
        heapq.heappush(self.heap, value)

    def extract_min(self) -> int:
        """Extrae el elemento mínimo."""
        return heapq.heappop(self.heap)

    def __iter__(self) -> Iterator[int]:
        """Permite recorrer los elementos del heap."""
        return iter(self.heap)


# Ejemplo
heap = MinHeap()

heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(2)

print(heap.extract_min())

for numero in heap:
    print(numero)