from flask import Flask, request, render_template, jsonify
from entities.asiento import Asiento
from entities.cliente import Cliente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_cliente', methods=['POST'])
def save_cliente():
    
    data = request.get_json()
    
    cliente = Cliente(id=0, nombre=data['nombre'], email=data['email'], asiento=data['asiento'])
    
    cliente.save()
    if cliente.id == 0:
        return jsonify({"success":True, "id":cliente.id}), 201
    else:
        return jsonify({"success" : False,}), 500


if __name__ == "__main__":
    app.run(port=5079, host='0.0.0.0')