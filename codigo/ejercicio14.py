import heapq
from typing import List, Tuple


class PriorityQueue:
    """
    Cola con prioridad para planificar tareas.
    """

    def __init__(self) -> None:
        self.queue: List[Tuple[int, str]] = []

    def add_task(self, priority: int, task: str) -> None:
        """Agrega una tarea con prioridad."""
        heapq.heappush(self.queue, (priority, task))

    def execute_task(self) -> str:
        """Ejecuta la tarea con mayor prioridad."""
        priority, task = heapq.heappop(self.queue)
        return task


# Ejemplo
scheduler = PriorityQueue()

scheduler.add_task(1, "Actualizar sistema")
scheduler.add_task(3, "Enviar correo")
scheduler.add_task(2, "Respaldar datos")

print(scheduler.execute_task())