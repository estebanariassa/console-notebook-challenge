# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code, title, text, importance, creation_date):

        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = creation_date
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        pass

    def __str__(self):
        return f'Date: {self.creation_date}\n{self.title}: {self.text}'

class Notebook:

    def __init__(self, notes):

        self.notes:list[notes] = []



