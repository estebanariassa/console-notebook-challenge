# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code, title, text, importance, creation_date):

        code: str = code
        title: str = title
        text: str = text
        importance: str = importance
        creation_date: datetime = creation_date