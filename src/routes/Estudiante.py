from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Estudiante import Estudiante
# Models
from models.EstudianteModel import EstudianteModel

main = Blueprint('estudiante_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_estudiantes():
    try:
        estudiantes = EstudianteModel.get_estudiantes()
        return jsonify(estudiantes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/<id>', methods=['GET'])
def get_estudiante(id_estudiante):
    try:
        estudiante = EstudianteModel.get_estudiante(id_estudiante)
        if estudiante != None:
            return jsonify(estudiante)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/add', methods=['POST'])
def add_estudiante():
    try:
        nombre_estudiante = request.json['nombre_estudiante']
        correo_estudiante = request.json['correo_estudiante']
        id_facultad = request.json['id_facultad']
        id_estudiante = uuid.uuid4()
        estudiante = Estudiante(str(id_estudiante), correo_estudiante, nombre_estudiante, id_facultad)
        
        affected_rows = EstudianteModel.add_estudiante(estudiante)

        if affected_rows == 1:
            return jsonify(estudiante.id_estudiante)
        else:
            return jsonify({'message': "Error al Insertar"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/update', methods=['PUT'])
def update_estudiante(id_estudiante):
    try:
        nombre_estudiante = request.json['nombre_estudiante']
        correo_estudiante = request.json['correo_estudiante']
        id_facultad = request.json['id_facultad']
        estudiante = Estudiante(id_estudiante, correo_estudiante, nombre_estudiante, id_facultad)
        
        affected_rows = EstudianteModel.update_estudiante(estudiante)

        if affected_rows == 1:
            return jsonify(estudiante.id_estudiante)
        else:
            return jsonify({'message': "Ningún estudiante actualizado."}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    

@main.route('/delete', methods=['DELETE'])
def delete_estudiante(id_estudiante):
    try:
        estudiante = Estudiante(id_estudiante)
        
        affected_rows = EstudianteModel.delete_estudiante(estudiante)

        if affected_rows == 1:
            return jsonify(estudiante.id_estudiante)
        else:
            return jsonify({'message': "Ningún estudiante borrado."}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500