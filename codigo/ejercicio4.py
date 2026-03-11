from typing import List


class NodoMenu:

    def __init__(self, opcion: str) -> None:
        self.opcion = opcion
        self.submenus: List["NodoMenu"] = []

    def agregar(self, nodo: "NodoMenu") -> None:
        self.submenus.append(nodo)


class Menu:

    def __init__(self, raiz: NodoMenu) -> None:
        self.raiz = raiz


def ejemplo_menu() -> Menu:

    menu_principal = NodoMenu("Menu")

    archivo = NodoMenu("Archivo")
    editar = NodoMenu("Editar")

    archivo.agregar(NodoMenu("Nuevo"))
    archivo.agregar(NodoMenu("Guardar"))

    editar.agregar(NodoMenu("Copiar"))
    editar.agregar(NodoMenu("Pegar"))

    menu_principal.agregar(archivo)
    menu_principal.agregar(editar)

    return Menu(menu_principal)