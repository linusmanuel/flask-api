from app import app
from flask import jsonify, Blueprint

bp_routes = Blueprint('routes', __name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Criando api com flask'})
