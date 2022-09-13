from flask import Flask, jsonify
from flask_cors import CORS
from config import config

# Routes
from routes import Estudiante

from users import users

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:3000"}})

def page_not_found(error):
    return "<h1>Página no encontrada</h1>", 404


@app.route('/users', methods=['GET'])
def usersHandler():
    return jsonify({"users": users})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(Estudiante.main, url_prefix ='/app/estudiantes')
    
    #Error handlers
    app.register_error_handler(404, page_not_found)
    
    app.run(host="0.0.0.0", port=4000, debug=True)
    
    
    
