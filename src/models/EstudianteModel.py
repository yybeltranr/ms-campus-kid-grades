from database.db import get_connection
from .entities.Estudiante import Estudiante

class EstudianteModel():
    
    @classmethod
    def get_estudiantes(self):
        try:
            connection = get_connection()
            estudiantes = []
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM estudiante")
                resultset = cursor.fetchall()
                
                for row in resultset:
                    estudiante = Estudiante(row[0], row[1], row[2], row[3]) 
                    estudiantes.append(estudiante.to_JSON())
                    
            connection.close()
            return estudiantes
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_estudiante(self, id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM estudiante WHERE id_estudiante = %s", (id,))
                row= cursor.fetchone()
                
                estudiante = None
                if row != None:
                    estudiante = Estudiante(row[0], row[1], row[2], row[3]) 
                    estudiante = estudiante.to_JSON()
                    
            connection.close()
            return estudiante
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def add_estudiante(self, estudiante):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO estudiante (id_estudiante, correo_estudiante, nombre_estudiante, id_facultad) VALUES (%s, %s, %s, %s)", (estudiante.id_estudiante, estudiante.correo_estudiante, estudiante.nombre_estudiante, estudiante.id_facultad))
                affected_rows= cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def update_estudiante(self, estudiante):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE estudiante SET correo_estudiante = %s, nombre_estudiante = %s, id_facultad = %s
                                WHERE id_estudiante = %s""", (estudiante.correo_estudiante, estudiante.nombre_estudiante, estudiante.id_facultad, estudiante.id_estudiante))
                affected_rows= cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def delete_estudiante(self, estudiante):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM estudiante WHERE id_estudiante = %s", (estudiante.id_estudiante,))
                affected_rows= cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)