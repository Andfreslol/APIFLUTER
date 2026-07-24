from flask import Flask, request, jsonify
from flask_cors import CORS

from config import Config
from models import db, Usuario

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()

# ==========================
# Obtener todos
# ==========================
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])

# ==========================
# Obtener por ID
# ==========================
@app.route("/usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

# ==========================
# Crear usuario
# ==========================
@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    datos = request.get_json()

    usuario = Usuario(
        nombre=datos["nombre"],
        correo=datos["correo"]
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify(usuario.to_dict()), 201

# ==========================
# Actualizar
# ==========================
@app.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    datos = request.get_json()

    usuario.nombre = datos["nombre"]
    usuario.correo = datos["correo"]

    db.session.commit()

    return jsonify(usuario.to_dict())

# ==========================
# Eliminar
# ==========================
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):

    usuario = Usuario.query.get_or_404(id)

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario eliminado"
    })

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API CRUD funcionando correctamente"
    })

if __name__ == "__main__":
    app.run(debug=True)