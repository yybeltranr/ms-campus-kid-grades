from utils.DateFormat import DateFormat

class Estudiante():
    
    def __init__(self, id_estudiante, correo_estudiante=None, nombre_estudiante=None, id_facultad=None) -> None:
        self.id_estudiante= id_estudiante
        self.correo_estudiante = correo_estudiante
        self.nombre_estudiante = nombre_estudiante
        self.id_facultad = id_facultad
        
    def to_JSON(self):
        return {
            'id_estudiante': self.id_estudiante,
            'correo_estudiante': self.correo_estudiante,
            'nombre_estudiante': self.nombre_estudiante,
            'id_facultad': self.id_facultad
        }