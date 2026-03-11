import heapq
from typing import List, Tuple


class NetworkQueue:
    """
    Simulación de una red donde los paquetes tienen prioridad.
    """

    def __init__(self) -> None:
        self.queue: List[Tuple[int, str]] = []

    def send_packet(self, priority: int, packet: str) -> None:
        """Agrega un paquete a la red."""
        heapq.heappush(self.queue, (priority, packet))

    def process_packet(self) -> str:
        """Procesa el paquete con mayor prioridad."""
        priority, packet = heapq.heappop(self.queue)
        return packet


# Ejemplo
network = NetworkQueue()

network.send_packet(1, "Video en tiempo real")
network.send_packet(3, "Correo electrónico")
network.send_packet(2, "Mensaje de chat")

print(network.process_packet())