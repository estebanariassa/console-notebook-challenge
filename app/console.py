# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from app.notebook import Notebook


class ConsoleUI:
    def __init__(self):
        self.notebook = Notebook()
        self.console = Console() # Usar la clase Console de rich
        self.main_menu()

def main_menu(self):
    while True:
        self.console.clear() # Limpiar la consola
        self.console.print("[bold blue]Cuaderno de Notas[/bold blue]", justify="center")
        self.console.print("[blue]1.[/blue] Agregar Nota")
        self.console.print("[blue]2.[/blue] Listar Notas")
        self.console.print("[blue]3.[/blue] Agregar Etiqueta a Nota")
        self.console.print("[blue]4.[/blue] Listar Notas Importantes")
        self.console.print("[blue]5.[/blue] Eliminar Nota")
        self.console.print("[blue]6.[/blue] Mostrar Notas por Etiqueta")
        self.console.print("[blue]7.[/blue] Mostrar Etiqueta con Más Notas")
        self.console.print("[green]8.[/green] Salir")

        choice = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

        if choice == "1":
            self.add_note()
        elif choice == "2":
            self.list_notes()
        elif choice == "3":
            self.add_tag_to_note()
        elif choice == "4":
            self.list_important_notes()
        elif choice == "5":
            self.delete_note()
        elif choice == "6":
            self.show_notes_by_tag()
        elif choice == "7":
            self.show_tag_with_most_notes()
        elif choice == "8":
            self.console.print("Saliendo...", style="bold red")
        break